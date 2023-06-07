from __future__ import annotations

from typing import *
from edg_core import *

import edgir
from edg_core import IdentityDict  # TODO: this is ugly
from edg_core.ConstraintExpr import Refable

@non_library
class MechBaseBlock(BaseBlock):
  def mech(self) -> None:
    """Defines all ports on this block as mechanical"""
    self.cons = self.Metadata({'_': '+'})  # TODO should be empty

@abstract_block
class MechanicalBlock(Block):
  """Block that represents a component that has part(s) and model(s).
  Provides interfaces that define shapes? and connections.
  """
  # TODO perhaps don't allow part / package initializers since those shouldn't be used
  def __init__(self) -> None:
    super().__init__()
    self.m_mass = self.Parameter(StringExpr())
    self.m_material = self.Parameter(StringExpr())
    self.m_method = self.Parameter(StringExpr())

    self.m_mfr = self.Parameter(StringExpr())
    self.m_partname = self.Parameter(StringExpr())
    self.m_desc = self.Parameter(StringExpr())
    self.m_datasheet = self.Parameter(StringExpr())

  # TODO: allow value to be taken from parameters, ideally w/ string concat from params
  def part(self, desc: StringLike,
                mfr: Optional[StringLike] = None, partname: Optional[StringLike] = None, datasheet: Optional[StringLike] = None,
                mass: Optional[StringLike] = None, material: Optional[StringLike] = None, method: Optional[StringLike] = None) -> None:
    """Creates a part in this mechanical block.
    Desc is a one-line description of the part, to be used as an aid during assembly"""
    from edg_core.Blocks import BlockElaborationState, BlockDefinitionError

    if self._elaboration_state not in (BlockElaborationState.init, BlockElaborationState.contents,
                                       BlockElaborationState.generate):
      raise BlockDefinitionError(self, "can't call part(...) outside __init__, contents or generate",
                                 "call part(...) inside those functions, and remember to make the super() call")

    self.m_is_mechanical = self.Metadata("m")

    self.assign(self.m_desc, desc)
    if mfr is not None:
      self.assign(self.m_mfr, mfr)
    else:
      self.assign(self.m_mfr, '')
    if partname is not None:
      self.assign(self.m_partname, partname)
    else:
      self.assign(self.m_partname, '')
    if datasheet is not None:
      self.assign(self.m_datasheet, datasheet)
    else:
      self.assign(self.m_datasheet, '')

    if mass is not None:
      self.assign(self.m_mass, mass)
    else:
      self.assign(self.m_mass, '')
    if material is not None:
      self.assign(self.m_material, material)
    else:
      self.assign(self.m_material, '')
    if method is not None:
      self.assign(self.m_method, method)
    else:
      self.assign(self.m_method, '')


@abstract_block
class MechBlock(MechBaseBlock, Block):
  def contents(self):
    super().contents()
    self.mech()

@abstract_block
class MechPortBridge(MechBaseBlock, PortBridge):
  def contents(self):
    super().contents()
    self.mech()

  def _get_ref_map(self, prefix: edgir.LocalPath) -> IdentityDict[Refable, edgir.LocalPath]:
    if self.__class__ == MechPortBridge:  # TODO: hack to allow this to elaborate as abstract class while being invalid
      return IdentityDict()
    return super()._get_ref_map(prefix)


# AdapterDstType = TypeVar('AdapterDstType', bound='CircuitPort')
# @abstract_block
# class CircuitPortAdapter(KiCadImportableBlock, NetBaseBlock, PortAdapter[AdapterDstType], Generic[AdapterDstType]):
#   def symbol_pinning(self, symbol_name: str) -> Dict[str, BasePort]:
#     assert symbol_name == 'edg_importable:Adapter'
#     return {'1': self.src, '2': self.dst}

#   def contents(self):
#     super().contents()
#     self.net()

#   def _get_ref_map(self, prefix: edgir.LocalPath) -> IdentityDict[Refable, edgir.LocalPath]:
#     if self.__class__ == CircuitPortAdapter:  # TODO: hack to allow this to elaborate as abstract class while being invalid
#       return IdentityDict()
#     return super()._get_ref_map(prefix)


@non_library  # TODO make abstract instead?
class MechLink(MechBaseBlock, Link):
  def contents(self):
    super().contents()
    self.mech()
