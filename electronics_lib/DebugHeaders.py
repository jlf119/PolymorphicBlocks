from electronics_abstract_parts import *
from .PassiveConnector import PinHeader127DualShrouded, TagConnect, PinHeader254DualShroudedInline


class SwdCortexTargetHeader(SwdCortexTargetWithSwoTdiConnector):
  def contents(self):
    super().contents()
    self.conn = self.Block(PinHeader127DualShrouded(10))
    self.connect(self.pwr, self.conn.pins.request('1').adapt_to(VoltageSink()))
    self.connect(self.gnd, self.conn.pins.request('3').adapt_to(Ground()),
                 self.conn.pins.request('5').adapt_to(Ground()),
                 self.conn.pins.request('9').adapt_to(Ground()))
    self.connect(self.swd.swdio, self.conn.pins.request('2').adapt_to(DigitalBidir()))
    self.connect(self.swd.swclk, self.conn.pins.request('4').adapt_to(DigitalSource()))
    self.connect(self.swo, self.conn.pins.request('6').adapt_to(DigitalBidir()))
    self.connect(self.tdi, self.conn.pins.request('8').adapt_to(DigitalBidir()))
    self.connect(self.swd.reset, self.conn.pins.request('10').adapt_to(DigitalSource()))


class SwdCortexTargetTagConnect(SwdCortexTargetWithSwoTdiConnector, Block):
  """OFFICIAL tag connect SWD header using the TC2030 series cables."""
  def contents(self):
    super().contents()
    self.conn = self.Block(TagConnect(6))
    self.connect(self.pwr, self.conn.pins.request('1').adapt_to(VoltageSink()))
    self.connect(self.swd.swdio, self.conn.pins.request('2').adapt_to(DigitalBidir()))  # also TMS
    self.connect(self.swd.reset, self.conn.pins.request('3').adapt_to(DigitalSource()))
    self.connect(self.swd.swclk, self.conn.pins.request('4').adapt_to(DigitalSource()))
    self.connect(self.gnd, self.conn.pins.request('5').adapt_to(Ground()))
    self.connect(self.swo, self.conn.pins.request('6').adapt_to(DigitalBidir()))
    # TODO the block shouldn't have TDI at all, but this maintains compatibility
    self.require(~self.tdi.is_connected())


class SwdCortexTargetTc2050(SwdCortexTargetWithSwoTdiConnector, Block):
  """UNOFFICIAL tag connect SWD header, maintaining physical pin compatibility with the 2x05 1.27mm header."""
  def contents(self):
    super().contents()
    self.conn = self.Block(TagConnect(10))
    self.connect(self.pwr, self.conn.pins.request('1').adapt_to(VoltageSink()))
    self.connect(self.gnd, self.conn.pins.request('2').adapt_to(Ground()),
                 self.conn.pins.request('3').adapt_to(Ground()),
                 self.conn.pins.request('5').adapt_to(Ground()))
    self.connect(self.swd.swdio, self.conn.pins.request('10').adapt_to(DigitalBidir()))
    self.connect(self.swd.swclk, self.conn.pins.request('9').adapt_to(DigitalSource()))
    self.connect(self.swo, self.conn.pins.request('8').adapt_to(DigitalBidir()))
    self.connect(self.tdi, self.conn.pins.request('7').adapt_to(DigitalBidir()))
    self.connect(self.swd.reset, self.conn.pins.request('6').adapt_to(DigitalSource()))
