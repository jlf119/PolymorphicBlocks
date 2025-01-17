import os
import inspect
from contextlib import suppress
from typing import Type, Optional, Tuple

from edg_core import Block, ScalaCompiler, CompiledDesign
from electronics_model import NetlistBackend, BomBackend
from electronics_model.RefdesRefinementPass import RefdesRefinementPass
from electronics_model.BomBackend import GenerateBom


def compile_board(design: Type[Block], target_dir_name: Optional[Tuple[str, str]]) -> CompiledDesign:
  if target_dir_name is not None:
    (target_dir, target_name) = target_dir_name
    if not os.path.exists(target_dir):
      os.makedirs(target_dir)
    assert os.path.isdir(target_dir), f"target_dir {target_dir} to compile_board must be directory"

    design_filename = os.path.join(target_dir, f'{target_name}.edg')
    netlist_filename = os.path.join(target_dir, f'{target_name}.net')
    bom_filename = os.path.join(target_dir, f'{target_name}.csv')

    with suppress(FileNotFoundError):
      os.remove(design_filename)
    with suppress(FileNotFoundError):
      os.remove(netlist_filename)
    with suppress(FileNotFoundError):
      os.remove(bom_filename)

  compiled = ScalaCompiler.compile(design)
  compiled.append_values(RefdesRefinementPass().run(compiled))
  netlist_all = NetlistBackend().run(compiled)
  bom_all = GenerateBom().run(compiled)
  assert len(netlist_all) == 1

  if target_dir_name is not None:
    with open(design_filename, 'wb') as raw_file:
      raw_file.write(compiled.design.SerializeToString())

    with open(netlist_filename, 'w', encoding='utf-8') as net_file:
      net_file.write(netlist_all[0][1])

    with open(bom_filename, 'w', encoding='utf-8') as bom_file:
      bom_file.write(bom_all[0][1])

  return compiled


def compile_board_inplace(design: Type[Block], generate: bool = True) -> CompiledDesign:
  """Compiles a board and writes the results in a sub-directory
  where the module containing the top-level is located"""
  designfile = inspect.getfile(design)
  if generate:
    target_dir_name = (os.path.join(os.path.dirname(designfile), design.__name__), design.__name__)
  else:
    target_dir_name = None
  compiled = compile_board(design, target_dir_name)

  return compiled
