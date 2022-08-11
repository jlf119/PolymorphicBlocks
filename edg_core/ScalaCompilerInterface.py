from typing import Optional, Any, Type, Iterable, Union, Dict

import os
import subprocess
import sys

import edgir
import edgrpc
from .BufferSerializer import BufferSerializer, BufferDeserializer
from .Core import builder
from .HierarchyBlock import Block
from .DesignTop import DesignTop
from .Refinements import Refinements


class CompilerCheckError(BaseException):
  pass


class CompiledDesign:
  @staticmethod
  def from_compiler_result(result: edgrpc.CompilerResult) -> 'CompiledDesign':
    values = {value.path.SerializeToString(): edgir.valuelit_to_lit(value.value)
              for value in result.solvedValues}
    return CompiledDesign(result.design, values)

  @staticmethod
  def from_backend_request(request: edgrpc.BackendRequest) -> 'CompiledDesign':
    values = {value.path.SerializeToString(): edgir.valuelit_to_lit(value.value)
              for value in request.solvedValues}
    return CompiledDesign(request.design, values)

  def __init__(self, design: edgir.Design, values: Dict[bytes, edgir.LitTypes]):
    self.design = design
    self.contents = design.contents  # convenience accessor
    self._values = values

  # Reserved.V is a string because it doesn't load properly at runtime
  # Serialized strings are used since proto objects are mutable and unhashable
  def get_value(self, path: Iterable[Union[str, 'edgir.Reserved.V']]) -> Optional[edgir.LitTypes]:
    path_key = edgir.LocalPathList(path).SerializeToString()
    return self._values.get(path_key, None)


class ScalaCompilerInstance:
  PRECOMPIED_RELPATH = "compiler/edg-compiler-precompiled.jar"
  DEV_RELPATH = "compiler/target/scala-2.13/edg-compiler-assembly-0.1-SNAPSHOT.jar"

  def __init__(self, *, suppress_stderr: bool = False):
    self.process: Optional[Any] = None
    self.suppress_stderr = suppress_stderr
    self.request_serializer: Optional[BufferSerializer[edgrpc.CompilerRequest]] = None
    self.response_deserializer: Optional[BufferDeserializer[edgrpc.CompilerResult]] = None

  def check_started(self) -> None:
    if self.process is None:
      if os.path.exists(self.DEV_RELPATH):
        jar_path = self.DEV_RELPATH
        print("Using development JAR")
      elif os.path.exists(self.PRECOMPIED_RELPATH):
        jar_path = self.PRECOMPIED_RELPATH
      else:
        raise ValueError("No EDG Compiler JAR found")

      self.process = subprocess.Popen(
        ['java', '-jar', jar_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE if self.suppress_stderr else None
      )

      assert self.process.stdin is not None
      self.request_serializer = BufferSerializer[edgrpc.CompilerRequest](self.process.stdin)
      assert self.process.stdout is not None
      self.response_deserializer = BufferDeserializer(edgrpc.CompilerResult, self.process.stdout)


  def compile(self, block: Type[Block], refinements: Refinements = Refinements()) -> CompiledDesign:
    self.check_started()
    assert self.request_serializer is not None
    assert self.response_deserializer is not None

    block_obj = block()
    request = edgrpc.CompilerRequest(
      modules=[block.__module__],
      design=edgir.Design(
        contents=builder.elaborate_toplevel(block_obj))
    )
    if isinstance(block_obj, DesignTop):
      refinements = block_obj.refinements() + refinements

    refinements.populate_proto(request.refinements)

    self.request_serializer.write(request)
    result = self.response_deserializer.read()

    sys.stdout.buffer.write(self.response_deserializer.read_stdout())
    sys.stdout.buffer.flush()

    assert result is not None
    if not result.HasField('design'):
      raise CompilerCheckError(f"no compiled result, with error {result.error}")
    if result.error:
      raise CompilerCheckError(f"error during compilation: \n{result.error}")
    return CompiledDesign.from_compiler_result(result)

  def close(self):
    assert self.process is not None
    self.process.stdin.close()
    self.process.stdout.close()
    if self.suppress_stderr:
      self.process.stderr.close()
    self.process.wait()


ScalaCompiler = ScalaCompilerInstance()
