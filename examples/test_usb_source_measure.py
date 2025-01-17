import unittest
from typing import Mapping, Optional

from electronics_abstract_parts.ESeriesUtil import ESeriesRatioUtil
from electronics_abstract_parts.ResistiveDivider import DividerValues
from electronics_model.VoltagePorts import VoltageSinkAdapterAnalogSource  # needed by imported schematic
from edg import *


class GatedEmitterFollower(InternalSubcircuit, KiCadSchematicBlock, KiCadImportableBlock, Block):
  """Emitter follower, where each transistor can have its input gated independently,
  and a transistor with a disabled input will turn off.

  For the SMU, this allows a turn-on scheme where the error integrated is railed to off one side,
  and only the off side transistor turns on, then the proper output can be programmed.
  After the output stabilizes, both transistors can be enabled (if desired), to run under the
  analog feedback circuit.
  """
  def symbol_pinning(self, symbol_name: str) -> Mapping[str, BasePort]:
    assert symbol_name == 'edg_importable:Opamp'  # this requires an schematic-modified symbol
    return {
      'IN': self.control, 'H': self.high_en, 'L': self.low_en,
      '3': self.out, 'V+': self.pwr, 'V-': self.gnd
    }

  @init_in_parent
  def __init__(self, current: RangeLike, rds_on: RangeLike):
    super().__init__()

    self.pwr = self.Port(VoltageSink.empty(), [Power])
    self.gnd = self.Port(Ground.empty(), [Common])
    self.out = self.Port(VoltageSource.empty())

    self.control = self.Port(AnalogSink.empty())
    self.high_en = self.Port(DigitalSink.empty())
    self.low_en = self.Port(DigitalSink.empty())

    self.current = self.ArgParameter(current)
    self.rds_on = self.ArgParameter(rds_on)

  def contents(self) -> None:
    super().contents()

    self.high_fet = self.Block(Fet.NFet(
      drain_voltage=self.pwr.link().voltage,
      drain_current=self.current,
      gate_voltage=self.control.link().voltage,
      rds_on=self.rds_on,
      gate_charge=RangeExpr.ALL,  # don't care, it's analog not switching
      power=self.pwr.link().voltage * self.current))
    self.low_fet = self.Block(Fet.PFet(
      drain_voltage=self.pwr.link().voltage,
      drain_current=self.current,
      gate_voltage=self.control.link().voltage,
      rds_on=self.rds_on,
      gate_charge=RangeExpr.ALL,  # don't care, it's analog not switching
      power=self.pwr.link().voltage * self.current))

    self.import_kicad(self.file_path("resources", f"{self.__class__.__name__}.kicad_sch"),
      conversions={
        'high_fet.D': VoltageSink(
          current_draw=self.current,
          voltage_limits=self.high_fet.actual_drain_voltage_rating.intersect(
            self.low_fet.actual_drain_voltage_rating)
        ),
        'high_fet.S': VoltageSource(
          voltage_out=self.pwr.link().voltage,
          current_limits=self.current
        ),
        'low_fet.S': VoltageSink(),  # ideal, modeled by high_fet source
        'low_fet.D': Ground(),

        'high_fet.G': AnalogSink(),
        'low_fet.G': AnalogSink(),

        'high_res.1': VoltageSink(),
        'low_res.1': VoltageSink(),

        'high_res.2': AnalogSource(),
        'low_res.2': AnalogSource(),
      })


class ErrorAmplifier(InternalSubcircuit, KiCadSchematicBlock, KiCadImportableBlock, GeneratorBlock):
  """Not really a general error amplifier circuit, but a subcircuit that performs that function in
  the context of this SMU analog feedback block.

  Consists of a resistive divider between the target and inverted sense signal, followed by
  an opamp follower circuit that is limited by either a resistor, or diode (for source-/sink-only operation).

  The target and sense signal should share a common reference ('zero') voltage, that is also the
  reference fed into the following integrator stage.
  When the measured signal is the same as the target, the sense input is equal-but-opposite from the
  target signal (referenced to the common reference), so the divider output is at common.
  Any deviation upsets this balance, which produces an error signal on the output.

  TODO: diode parameter should be an enum. Current values: '' (no diode), 'sink', 'source' (sinks or sources current)
  """
  def symbol_pinning(self, symbol_name: str) -> Mapping[str, BasePort]:
    assert symbol_name in ('Simulation_SPICE:OPAMP', 'edg_importable:Opamp')
    return {'+': self.actual, '-': self.target, '3': self.output, 'V+': self.pwr, 'V-': self.gnd}

  @init_in_parent
  def __init__(self, diode_spec: StringLike, output_resistance: RangeLike, input_resistance: RangeLike, *,
               series: IntLike = Default(24), tolerance: FloatLike = Default(0.01)):
    super().__init__()

    self.pwr = self.Port(VoltageSink.empty(), [Power])
    self.gnd = self.Port(Ground.empty(), [Common])

    self.target = self.Port(AnalogSink.empty())
    self.actual = self.Port(AnalogSink.empty())
    self.output = self.Port(AnalogSource.empty())

    self.output_resistance = self.ArgParameter(output_resistance)
    self.input_resistance = self.ArgParameter(input_resistance)
    self.diode_spec = self.ArgParameter(diode_spec)
    self.series = self.ArgParameter(series)
    self.tolerance = self.ArgParameter(tolerance)
    self.generator_param(self.input_resistance, self.diode_spec, self.series, self.tolerance)

  def generate(self) -> None:
    super().generate()

    # The 1/4 factor is a way to specify the series resistance of the divider assuming both resistors are equal,
    # since the DividerValues util only takes the parallel resistance
    calculator = ESeriesRatioUtil(ESeriesUtil.SERIES[self.get(self.series)], self.get(self.tolerance), DividerValues)
    top_resistance, bottom_resistance = calculator.find(DividerValues(Range.from_tolerance(0.5, self.get(self.tolerance)),
                                                                      self.get(self.input_resistance) / 4))

    self.amp = self.Block(Opamp())
    self.rtop = self.Block(Resistor(resistance=Range.from_tolerance(top_resistance, self.get(self.tolerance))))
    self.rbot = self.Block(Resistor(resistance=Range.from_tolerance(bottom_resistance, self.get(self.tolerance))))
    self.rout = self.Block(Resistor(resistance=self.output_resistance))

    diode_spec = self.get(self.diode_spec)
    if diode_spec:
      self.diode = self.Block(Diode(  # TODO should be encoded as a voltage difference?
        reverse_voltage=self.amp.out.voltage_out,
        current=RangeExpr.ZERO,  # an approximation, current rating not significant here
        voltage_drop=(0, 0.5)*Volt,  # arbitrary low threshold
        reverse_recovery_time=(0, 500)*nSecond  # arbitrary for "fast recovery"
      ))
      # regardless of diode direction, the port model is the same on both ends
      amp_out_model = AnalogSink(
        impedance=self.rout.actual_resistance + self.output.link().sink_impedance
      )
      rout_in_model = AnalogSource(
        impedance=self.amp.out.link().source_impedance + self.rout.actual_resistance
      )
      if diode_spec == 'source':
        nodes: Mapping[str, Optional[BasePort]] = {
          'amp_out_node': self.diode.anode.adapt_to(amp_out_model),
          'rout_in_node': self.diode.cathode.adapt_to(rout_in_model)
        }
      elif diode_spec == 'sink':
        nodes = {
          'amp_out_node': self.diode.cathode.adapt_to(amp_out_model),
          'rout_in_node': self.diode.anode.adapt_to(rout_in_model)
        }
      else:
        raise ValueError(f"invalid diode spec '{diode_spec}', expected '', 'source', or 'sink'")
    else:
      nodes = {
        'rout_in_node': self.amp.out,
        'amp_out_node': None,  # must be marked as used, but don't want to double-connect to above
      }

    self.import_kicad(self.file_path("resources", f"{self.__class__.__name__}.kicad_sch"),
        conversions={
          'rtop.1': AnalogSink(
            impedance=self.rtop.actual_resistance + self.rbot.actual_resistance
          ),
          'rbot.1': AnalogSink(
            impedance=self.rtop.actual_resistance + self.rbot.actual_resistance
          ),
          'rtop.2': AnalogSource(
            voltage_out=self.target.link().voltage.hull(self.actual.link().voltage),
            impedance=1 / (1 / self.rtop.actual_resistance + 1 / self.rbot.actual_resistance)
          ),
          'rbot.2': AnalogSink(),  # ideal, rtop.2 contains the parameter model
          'rout.1': AnalogSink(),
          'rout.2': AnalogSource(
            voltage_out=self.amp.out.link().voltage,
            impedance=self.rout.actual_resistance
          ),
        }, nodes=nodes)


class SourceMeasureControl(KiCadSchematicBlock, Block):
  """Analog feedback circuit for the source-measure unit
  """
  @init_in_parent
  def __init__(self, current: RangeLike, rds_on: RangeLike):
    super().__init__()

    self.pwr = self.Port(VoltageSink.empty(), [Power])
    self.pwr_logic = self.Port(VoltageSink.empty())
    self.gnd = self.Port(Ground.empty(), [Common])
    self.ref_center = self.Port(AnalogSink.empty())

    self.control_voltage = self.Port(AnalogSink.empty())
    self.control_current_source = self.Port(AnalogSink.empty())
    self.control_current_sink = self.Port(AnalogSink.empty())
    self.high_en = self.Port(DigitalSink.empty())
    self.low_en = self.Port(DigitalSink.empty())
    self.out = self.Port(VoltageSource.empty())

    self.measured_voltage = self.Port(AnalogSource.empty())
    self.measured_current = self.Port(AnalogSource.empty())

    self.current = self.ArgParameter(current)
    self.rds_on = self.ArgParameter(rds_on)

  def contents(self):
    super().contents()
    self.import_kicad(self.file_path("resources", f"{self.__class__.__name__}.kicad_sch"),
      locals={
        'err_volt': {
          'output_resistance': 4.7*kOhm(tol=0.05),
          'input_resistance': (10, 100)*kOhm
        },
        'err_current': {
          'output_resistance': 1*Ohm(tol=0.05),
          'input_resistance': (10, 100)*kOhm,
        },
        'int': {
          'factor': Range.from_tolerance(1 / 4.7e-6, 0.15),
          'capacitance': 1*nFarad(tol=0.15)
        },
        'amp': {
          'amplification': Range.from_tolerance(20, 0.05),
          'impedance': (1, 10)*kOhm
        },
        'driver': {
          'current': self.current,
          'rds_on': self.rds_on
        },
        'imeas': {
          'resistance': 0.1*Ohm(tol=0.01),
          'ratio': Range.from_tolerance(1, 0.05),
          'input_impedance': 10*kOhm(tol=0.05)
        },
        'vmeas': {
          'ratio': Range.from_tolerance(1/22, 0.05),
          'input_impedance': 220*kOhm(tol=0.05)
        },
      })


class UsbSourceMeasure(JlcBoardTop):
  def contents(self) -> None:
    super().contents()

    # overall design parameters
    CURRENT_RATING = (0, 3)*Amp

    # USB PD port that supplies power to the load
    # TODO the transistor is only rated at Vgs=+/-20V
    self.pwr_usb = self.Block(UsbCReceptacle(voltage_out=(4.5, 20)*Volt, current_limits=(0, 5)*Amp))

    # Data-only USB port, for example to connect to a computer that can't source USB PD
    # so the PD port can be connected to a dedicated power brick.
    self.data_usb = self.Block(UsbCReceptacle())

    # TODO next revision: add a USB data port switch so the PD port can also take data

    self.gnd_merge = self.Block(MergedVoltageSource()).connected_from(
      self.pwr_usb.gnd, self.data_usb.gnd)

    self.gnd = self.connect(self.gnd_merge.pwr_out)
    self.vusb = self.connect(self.pwr_usb.pwr)

    with self.implicit_connect(
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      (self.reg_5v, self.reg_3v3, self.led_3v3), _ = self.chain(
        self.vusb,
        imp.Block(BuckConverter(output_voltage=5.0*Volt(tol=0.05))),
        imp.Block(LinearRegulator(output_voltage=3.3*Volt(tol=0.05))),
        imp.Block(VoltageIndicatorLed())
      )
      self.v5 = self.connect(self.reg_5v.pwr_out)
      self.v3v3 = self.connect(self.reg_3v3.pwr_out)

      (self.reg_analog, self.led_analog), _ = self.chain(
        self.v5,
        imp.Block(LinearRegulator(output_voltage=3.0*Volt(tol=0.05))),
        imp.Block(VoltageIndicatorLed())
      )
      self.vanalog = self.connect(self.reg_analog.pwr_out)

      (self.ref_div, self.ref_buf), _ = self.chain(
        self.vanalog,
        imp.Block(VoltageDivider(output_voltage=1.5*Volt(tol=0.05), impedance=(10, 100)*kOhm)),
        imp.Block(OpampFollower())
      )
      self.connect(self.vanalog, self.ref_buf.pwr)
      self.vcenter = self.connect(self.ref_buf.output)

    with self.implicit_connect(
        ImplicitConnect(self.vusb, [Power]),
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      self.control = imp.Block(SourceMeasureControl(
        current=CURRENT_RATING,
        rds_on=(0, 0.2)*Ohm
      ))
      self.connect(self.v3v3, self.control.pwr_logic)
      self.connect(self.vcenter, self.control.ref_center)

    with self.implicit_connect(
        ImplicitConnect(self.v3v3, [Power]),
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      self.prot_3v3 = imp.Block(ProtectionZenerDiode(voltage=(3.45, 3.75)*Volt))

      # TODO next revision: optional clamping diode on CC lines (as present in PD buddy sink, but not OtterPill)
      self.pd = imp.Block(Fusb302b())
      self.connect(self.pwr_usb.pwr, self.pd.vbus)
      self.connect(self.pwr_usb.cc, self.pd.cc)

      self.mcu = imp.Block(IoController())

      (self.usb_esd, ), _ = self.chain(self.data_usb.usb, imp.Block(UsbEsdDiode()), self.mcu.usb.request())

      (self.i2c_pull, ), _ = self.chain(self.mcu.i2c.request(), imp.Block(I2cPullup()), self.pd.i2c)
      self.connect(self.mcu.gpio.request('pd_int'), self.pd.int)

      self.rgb = imp.Block(IndicatorSinkRgbLed())
      self.connect(self.mcu.gpio.request_vector('rgb'), self.rgb.signals)

      (self.sw1, ), _ = self.chain(imp.Block(DigitalSwitch()), self.mcu.gpio.request('sw1'))
      (self.sw2, ), _ = self.chain(imp.Block(DigitalSwitch()), self.mcu.gpio.request('sw2'))
      (self.sw3, ), _ = self.chain(imp.Block(DigitalSwitch()), self.mcu.gpio.request('sw3'))

      # TODO next revision: Blackberry trackball UI, speakers?

      shared_spi = self.mcu.spi.request('spi')

      self.lcd = imp.Block(Qt096t_if09())
      self.connect(self.reg_3v3.pwr_out.as_digital_source(), self.lcd.led)
      self.connect(self.mcu.gpio.request('lcd_reset'), self.lcd.reset)
      self.connect(self.mcu.gpio.request('lcd_rs'), self.lcd.rs)
      self.connect(shared_spi, self.lcd.spi)  # MISO unused
      self.connect(self.mcu.gpio.request('lcd_cs'), self.lcd.cs)

      (self.dac_v, ), _ = self.chain(shared_spi, imp.Block(Mcp4921()),
                                     self.control.control_voltage)
      (self.dac_ip, ), _ = self.chain(shared_spi, imp.Block(Mcp4921()),
                                      self.control.control_current_source)
      (self.dac_in, ), _ = self.chain(shared_spi, imp.Block(Mcp4921()),
                                      self.control.control_current_sink)

      (self.adc_v, ), _ = self.chain(self.control.measured_voltage, imp.Block(Mcp3201()),
                                     shared_spi)
      (self.adc_i, ), _ = self.chain(self.control.measured_current, imp.Block(Mcp3201()),
                                     shared_spi)

      self.connect(self.vanalog,
                   self.dac_v.ref, self.dac_ip.ref, self.dac_in.ref,
                   self.adc_v.ref, self.adc_i.ref)

      self.connect(self.mcu.gpio.request('dac_v_cs'), self.dac_v.cs)
      self.connect(self.mcu.gpio.request('dac_ip_cs'), self.dac_ip.cs)
      self.connect(self.mcu.gpio.request('dac_in_cs'), self.dac_in.cs)
      self.connect(self.mcu.gpio.request('adc_v_cs'), self.adc_v.cs)
      self.connect(self.mcu.gpio.request('adc_i_cs'), self.adc_i.cs)
      self.connect(self.mcu.gpio.request('dac_ldac'),
                   self.dac_v.ldac, self.dac_ip.ldac, self.dac_in.ldac)

      self.connect(self.mcu.gpio.request('high_en'), self.control.high_en)
      self.connect(self.mcu.gpio.request('low_en'), self.control.low_en)

    self.outn = self.Block(BananaSafetyJack())
    self.connect(self.gnd, self.outn.port.adapt_to(Ground()))
    self.outp = self.Block(BananaSafetyJack())
    self.connect(self.outp.port.adapt_to(VoltageSink(
      current_draw=CURRENT_RATING
    )), self.control.out)

    # TODO next revision: add high precision ADCs

    # Misc board
    self.duck = self.Block(DuckLogo())
    self.leadfree = self.Block(LeadFreeIndicator())
    self.id = self.Block(IdDots4())

  def refinements(self) -> Refinements:
    return super().refinements() + Refinements(
      instance_refinements=[
        (['mcu'], Lpc1549_48),
        (['reg_5v'], Tps54202h),
        (['reg_3v3'], Xc6209),
        (['reg_analog'], Ap2210),
        (['control', 'amp', 'amp'], Opa197),
        (['control', 'imeas', 'amp', 'amp'], Opa197),
        (['control', 'vmeas', 'amp'], Opa197),
        (['control', 'imeas', 'sense', 'res', 'res'], GenericChipResistor),  # big one not from JLC
        (['control', 'int', 'c'], GenericMlcc),  # no 1nF basic parts from JLC
        (['control', 'driver', 'low_fet'], CustomFet),
        (['control', 'driver', 'high_fet'], CustomFet),
      ],
      instance_values=[
        (['mcu', 'pin_assigns'], [
          'pd_int=28',
          'sw1=43',
          'sw2=44',
          'sw3=45',
          'rgb_blue=46',
          'rgb_green=47',
          'rgb_red=48',

          'dac_ldac=1',
          'dac_in_cs=2',
          'dac_ip_cs=3',
          'spi.mosi=4',
          'spi.miso=6',
          'spi.sck=7',
          'adc_v_cs=8',
          'adc_i_cs=12',
          'dac_v_cs=13',

          'lcd_reset=15',
          'lcd_rs=18',
          'lcd_cs=21',

          'low_en=22',
          'high_en=23',
        ]),
        (['mcu', 'swd_swo_pin'], 'PIO0_8'),
        # allow the regulator to go into tracking mode
        (['reg_5v', 'power_path', 'dutycycle_limit'], Range(0, float('inf'))),
        (['reg_5v', 'power_path', 'inductor_current_ripple'], Range(0.01, 0.5)),  # trade higher Imax for lower L
        # JLC does not have frequency specs, must be checked TODO
        (['reg_5v', 'power_path', 'inductor', 'ignore_frequency'], True),

        # NFET option: SQJ148EP-T1_GE3, NPN BJT option: PHPT60410NYX
        (['control', 'driver', 'high_fet', 'footprint_spec'], 'Package_SO:PowerPAK_SO-8_Single'),
        (['control', 'driver', 'high_fet', 'manufacturer_spec'], 'Vishay Siliconix'),
        (['control', 'driver', 'high_fet', 'part_spec'], 'SQJ148EP-T1_GE3'),
        (['control', 'driver', 'high_fet', 'power'], Range(0, 0)),
        # PFET option: SQJ431EP-T1_GE3, PNP BJT option: PHPT60410PYX
        (['control', 'driver', 'low_fet', 'footprint_spec'], 'Package_SO:PowerPAK_SO-8_Single'),
        (['control', 'driver', 'low_fet', 'manufacturer_spec'], 'Vishay Siliconix'),
        (['control', 'driver', 'low_fet', 'part_spec'], 'SQJ431EP-T1_GE3'),
        (['control', 'driver', 'low_fet', 'power'], Range(0, 0)),
        (['control', 'int_link', 'sink_impedance'], RangeExpr.INF),  # waive impedance check for integrator in
        (['control', 'int', 'c', 'footprint_spec'], 'Capacitor_SMD:C_0603_1608Metric'),
      ],
      class_refinements=[
        (SwdCortexTargetWithSwoTdiConnector, SwdCortexTargetTc2050),
        (Opamp, Tlv9061),  # higher precision opamps
        (SolidStateRelay, G3VM_61GR2),
        (BananaSafetyJack, Ct3151),
      ],
    )


class UsbSourceMeasureTestCase(unittest.TestCase):
  def test_design(self) -> None:
    compile_board_inplace(UsbSourceMeasure)
