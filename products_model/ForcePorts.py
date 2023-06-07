from __future__ import annotations

from typing import *
from edg_core import *
from edg_core.Blocks import DescriptionString
from .ProductBlock import MechLink, MechPortBridge
from .Units import Newton, Second


class ForceLink(MechLink):
  def __init__(self) -> None:
    super().__init__()

    self.source = self.Port(ForceSource())
    self.push = self.Port(Vector(ForcePush()))

    self.force = self.Parameter(RangeExpr())
    self.force_limits = self.Parameter(RangeExpr())

    self.description = DescriptionString(
      "<b>Force</b>: ", DescriptionString.FormatUnits(self.force, "N"),
      " <b>of limits</b>: ", DescriptionString.FormatUnits(self.force_limits, "N"))

  def contents(self) -> None:
    super().contents()

    self.assign(self.force, self.source.force_out)
    self.assign(self.force_limits, self.push.intersection(lambda x: x.force_limits))
    self.require(self.force_limits.contains(self.force), "incorrect force")


class ForcePushBridge(MechPortBridge):
  def __init__(self) -> None:
    super().__init__()

    self.outer_port = self.Port(ForcePush(force_limits=RangeExpr()))

    # Here we ignore the current_limits of the inner port, instead relying on the main link to handle it
    # The outer port's voltage_limits is untouched and should be defined in the port def.
    # TODO: it's a slightly optimization to handle them here. Should it be done?
    # TODO: or maybe current_limits / voltage_limits shouldn't be a port, but rather a block property?
    self.inner_link = self.Port(ForceSource(force_out=RangeExpr()))

  def contents(self) -> None:
    super().contents()

    self.assign(self.outer_port.force_limits, self.inner_link.link().force_limits)

    self.assign(self.inner_link.force_out, self.outer_port.link().force)


class ForceSourceBridge(MechPortBridge):  # basic passthrough port, sources look the same inside and outside
  def __init__(self) -> None:
    super().__init__()

    self.outer_port = self.Port(ForceSource(force_out=RangeExpr()))

    # Here we ignore the voltage_limits of the inner port, instead relying on the main link to handle it
    # The outer port's current_limits is untouched and should be defined in tte port def.
    # TODO: it's a slightly optimization to handle them here. Should it be done?
    # TODO: or maybe current_limits / voltage_limits shouldn't be a port, but rather a block property?
    self.inner_link = self.Port(ForcePush(force_limits=RangeExpr.ALL))

  def contents(self) -> None:
    super().contents()

    self.assign(self.outer_port.force_out, self.inner_link.link().force)


ForceLinkType = TypeVar('ForceLinkType', bound=Link)
class ForcePort(Port[ForceLinkType], Generic[ForceLinkType]):
  """Force connection that represents a single force into a single mechanical port"""
  pass


class ForceBase(ForcePort[ForceLink]):
  def __init__(self) -> None:
    super().__init__()
    self.link_type = ForceLink

#     self.isolation_domain = self.Parameter(RefParameter())  # semantics TBD
#     self.reference = self.Parameter(RefParameter())  # semantics TBD, ideally some concept of implicit domains



class ForcePush(ForceBase):
  def __init__(self, force_limits: RangeLike = Default(RangeExpr.ALL)) -> None:
    super().__init__()
    self.bridge_type = ForcePushBridge

    self.force_limits: RangeExpr = self.Parameter(RangeExpr(force_limits))


class ForceSource(ForceBase):
  def __init__(self, force_out: RangeLike = Default(RangeExpr.EMPTY_ZERO)) -> None:
    super().__init__()
    self.bridge_type = ForceSourceBridge

    self.force_out: RangeExpr = self.Parameter(RangeExpr(force_out))


Power = PortTag(ForcePush)  # General positive voltage port, should only be mutually exclusive with the below


# Note: in the current model, no explicit "power tag" is equivalent to digital / noisy supply
# TODO bring these back, on an optional basis
# PowerAnalog = PortTag(VoltageSink)  # Analog power supply, ideally kept isolated from digital supply
# PowerRf = PortTag(VoltageSink)  # RF power supply
# Power1v8 = PortTag(VoltageSink)  # 1.8v tolerant power input port
# Power2v5 = PortTag(VoltageSink)  # 2.5v tolerant power input port
# Power3v3 = PortTag(VoltageSink)  # 3.3v tolerant power input port
# Power5v = PortTag(VoltageSink)  # 5.0v tolerant power input port
# Power12v = PortTag(VoltageSink)  # 12v tolerant power input port
