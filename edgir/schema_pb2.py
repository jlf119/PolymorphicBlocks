# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edgir/schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from edgir import common_pb2 as edgir_dot_common__pb2
from edgir import elem_pb2 as edgir_dot_elem__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x65\x64gir/schema.proto\x12\x0c\x65\x64gir.schema\x1a\x12\x65\x64gir/common.proto\x1a\x10\x65\x64gir/elem.proto\"\x9b\x04\n\x07Library\x12*\n\x02id\x18\x01 \x01(\x0b\x32\x1e.edgir.schema.Library.LibIdent\x12\x0f\n\x07imports\x18\x02 \x03(\t\x12&\n\x04root\x18\n \x01(\x0b\x32\x18.edgir.schema.Library.NS\x12$\n\x04meta\x18\x7f \x01(\x0b\x32\x16.edgir.common.Metadata\x1a\xea\x02\n\x02NS\x12\x36\n\x07members\x18\x01 \x03(\x0b\x32%.edgir.schema.Library.NS.MembersEntry\x1a\xdd\x01\n\x03Val\x12 \n\x04port\x18\n \x01(\x0b\x32\x10.edgir.elem.PortH\x00\x12$\n\x06\x62undle\x18\x0b \x01(\x0b\x32\x12.edgir.elem.BundleH\x00\x12\x35\n\x0fhierarchy_block\x18\r \x01(\x0b\x32\x1a.edgir.elem.HierarchyBlockH\x00\x12 \n\x04link\x18\x0e \x01(\x0b\x32\x10.edgir.elem.LinkH\x00\x12-\n\tnamespace\x18\x14 \x01(\x0b\x32\x18.edgir.schema.Library.NSH\x00\x42\x06\n\x04type\x1aL\n\x0cMembersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.edgir.schema.Library.NS.Val:\x02\x38\x01\x1a\x18\n\x08LibIdent\x12\x0c\n\x04name\x18\x01 \x01(\t\"6\n\x06\x44\x65sign\x12,\n\x08\x63ontents\x18\x02 \x01(\x0b\x32\x1a.edgir.elem.HierarchyBlockb\x06proto3')



_LIBRARY = DESCRIPTOR.message_types_by_name['Library']
_LIBRARY_NS = _LIBRARY.nested_types_by_name['NS']
_LIBRARY_NS_VAL = _LIBRARY_NS.nested_types_by_name['Val']
_LIBRARY_NS_MEMBERSENTRY = _LIBRARY_NS.nested_types_by_name['MembersEntry']
_LIBRARY_LIBIDENT = _LIBRARY.nested_types_by_name['LibIdent']
_DESIGN = DESCRIPTOR.message_types_by_name['Design']
Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), {

  'NS' : _reflection.GeneratedProtocolMessageType('NS', (_message.Message,), {

    'Val' : _reflection.GeneratedProtocolMessageType('Val', (_message.Message,), {
      'DESCRIPTOR' : _LIBRARY_NS_VAL,
      '__module__' : 'edgir.schema_pb2'
      # @@protoc_insertion_point(class_scope:edgir.schema.Library.NS.Val)
      })
    ,

    'MembersEntry' : _reflection.GeneratedProtocolMessageType('MembersEntry', (_message.Message,), {
      'DESCRIPTOR' : _LIBRARY_NS_MEMBERSENTRY,
      '__module__' : 'edgir.schema_pb2'
      # @@protoc_insertion_point(class_scope:edgir.schema.Library.NS.MembersEntry)
      })
    ,
    'DESCRIPTOR' : _LIBRARY_NS,
    '__module__' : 'edgir.schema_pb2'
    # @@protoc_insertion_point(class_scope:edgir.schema.Library.NS)
    })
  ,

  'LibIdent' : _reflection.GeneratedProtocolMessageType('LibIdent', (_message.Message,), {
    'DESCRIPTOR' : _LIBRARY_LIBIDENT,
    '__module__' : 'edgir.schema_pb2'
    # @@protoc_insertion_point(class_scope:edgir.schema.Library.LibIdent)
    })
  ,
  'DESCRIPTOR' : _LIBRARY,
  '__module__' : 'edgir.schema_pb2'
  # @@protoc_insertion_point(class_scope:edgir.schema.Library)
  })
_sym_db.RegisterMessage(Library)
_sym_db.RegisterMessage(Library.NS)
_sym_db.RegisterMessage(Library.NS.Val)
_sym_db.RegisterMessage(Library.NS.MembersEntry)
_sym_db.RegisterMessage(Library.LibIdent)

Design = _reflection.GeneratedProtocolMessageType('Design', (_message.Message,), {
  'DESCRIPTOR' : _DESIGN,
  '__module__' : 'edgir.schema_pb2'
  # @@protoc_insertion_point(class_scope:edgir.schema.Design)
  })
_sym_db.RegisterMessage(Design)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIBRARY_NS_MEMBERSENTRY._options = None
  _LIBRARY_NS_MEMBERSENTRY._serialized_options = b'8\001'
  _LIBRARY._serialized_start=75
  _LIBRARY._serialized_end=614
  _LIBRARY_NS._serialized_start=226
  _LIBRARY_NS._serialized_end=588
  _LIBRARY_NS_VAL._serialized_start=289
  _LIBRARY_NS_VAL._serialized_end=510
  _LIBRARY_NS_MEMBERSENTRY._serialized_start=512
  _LIBRARY_NS_MEMBERSENTRY._serialized_end=588
  _LIBRARY_LIBIDENT._serialized_start=590
  _LIBRARY_LIBIDENT._serialized_end=614
  _DESIGN._serialized_start=616
  _DESIGN._serialized_end=670
# @@protoc_insertion_point(module_scope)