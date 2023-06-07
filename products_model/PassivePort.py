from __future__ import annotations

from typing import *
from edg_core import *
from edg_core.Blocks import DescriptionString
from .ProductBlock import MechLink, MechPortBridge
from .Units import Newton, Second


class PassiveMechLink(MechLink):
  def __init__(self) -> None:
    super().__init__()

    self.source = self.Port(PassiveMech())
    self.sink = self.Port(PassiveMech())

    # self.description = DescriptionString(
    #   "<b>Force</b>: ", DescriptionString.FormatUnits(self.force, "N"),
    #   " <b>of limits</b>: ", DescriptionString.FormatUnits(self.force_limits, "N"))

  def contents(self) -> None:
    super().contents()

    # self.assign(self.force, self.source.force_out)
    # self.assign(self.force_limits, self.push.intersection(lambda x: x.force_limits))


# class ForcePushBridge(MechPortBridge):
#   def __init__(self) -> None:
#     super().__init__()

#     self.outer_port = self.Port(ForcePush(force_limits=RangeExpr()))

#     # Here we ignore the current_limits of the inner port, instead relying on the main link to handle it
#     # The outer port's voltage_limits is untouched and should be defined in the port def.
#     # TODO: it's a slightly optimization to handle them here. Should it be done?
#     # TODO: or maybe current_limits / voltage_limits shouldn't be a port, but rather a block property?
#     self.inner_link = self.Port(ForceSource(force_out=RangeExpr()))

#   def contents(self) -> None:
#     super().contents()

#     self.assign(self.outer_port.force_limits, self.inner_link.link().force_limits)

#     self.assign(self.inner_link.force_out, self.outer_port.link().force)


class PassiveMechBridge(MechPortBridge):  # basic passthrough port, sources look the same inside and outside
  def __init__(self) -> None:
    super().__init__()

    self.outer_port = self.Port(PassiveMech())
    self.inner_link = self.Port(PassiveMech())

  def contents(self) -> None:
    super().contents()

    #self.assign(self.outer_port.force_out, self.inner_link.link().force)


PassiveMechLinkType = TypeVar('PassiveMechLinkType', bound=Link)
class PassiveMechPort(Port[PassiveMechLinkType], Generic[PassiveMechLinkType]):
  """Force connection that represents a single force into a single mechanical port"""
  pass


class PassiveMechBase(PassiveMechPort[PassiveMechLink]):
  def __init__(self) -> None:
    super().__init__()
    self.link_type = PassiveMechLink

#     self.isolation_domain = self.Parameter(RefParameter())  # semantics TBD
#     self.reference = self.Parameter(RefParameter())  # semantics TBD, ideally some concept of implicit domains

class PassiveMech(PassiveMechBase):
  def __init__(self) -> None:
    super().__init__()
    self.bridge_type = PassiveMechBridge

#Power = PortTag(ForcePush)  # General positive voltage port, should only be mutually exclusive with the below


# Note: in the current model, no explicit "power tag" is equivalent to digital / noisy supply
# TODO bring these back, on an optional basis
# PowerAnalog = PortTag(VoltageSink)  # Analog power supply, ideally kept isolated from digital supply
# PowerRf = PortTag(VoltageSink)  # RF power supply
# Power1v8 = PortTag(VoltageSink)  # 1.8v tolerant power input port
# Power2v5 = PortTag(VoltageSink)  # 2.5v tolerant power input port
# Power3v3 = PortTag(VoltageSink)  # 3.3v tolerant power input port
# Power5v = PortTag(VoltageSink)  # 5.0v tolerant power input port
# Power12v = PortTag(VoltageSink)  # 12v tolerant power input port
