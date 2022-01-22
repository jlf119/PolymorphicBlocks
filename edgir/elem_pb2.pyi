"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import edgir.common_pb2
import edgir.expr_pb2
import edgir.init_pb2
import edgir.ref_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Port(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ParamsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.init_pb2.ValInit: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.init_pb2.ValInit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.expr_pb2.ValueExpr: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.expr_pb2.ValueExpr] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    PARAMS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    SELF_CLASS_FIELD_NUMBER: builtins.int
    SUPERCLASSES_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.init_pb2.ValInit]: ...
    @property
    def constraints(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.expr_pb2.ValueExpr]: ...
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # superclasses, may be empty
    @property
    def superclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]: ...
    # TODO: this provides type hierarchy data only, inheritance semantics are currently undefined

    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        params : typing.Optional[typing.Mapping[typing.Text, edgir.init_pb2.ValInit]] = ...,
        constraints : typing.Optional[typing.Mapping[typing.Text, edgir.expr_pb2.ValueExpr]] = ...,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        superclasses : typing.Optional[typing.Iterable[edgir.ref_pb2.LibraryPath]] = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"constraints",b"constraints",u"meta",b"meta",u"params",b"params",u"self_class",b"self_class",u"superclasses",b"superclasses"]) -> None: ...
global___Port = Port

class Bundle(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ParamsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.init_pb2.ValInit: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.init_pb2.ValInit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___PortLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___PortLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.expr_pb2.ValueExpr: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.expr_pb2.ValueExpr] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    PARAMS_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    SELF_CLASS_FIELD_NUMBER: builtins.int
    SUPERCLASSES_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.init_pb2.ValInit]: ...
    @property
    def ports(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PortLike]: ...
    @property
    def constraints(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.expr_pb2.ValueExpr]: ...
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # superclasses, may be empty
    @property
    def superclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]: ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        params : typing.Optional[typing.Mapping[typing.Text, edgir.init_pb2.ValInit]] = ...,
        ports : typing.Optional[typing.Mapping[typing.Text, global___PortLike]] = ...,
        constraints : typing.Optional[typing.Mapping[typing.Text, edgir.expr_pb2.ValueExpr]] = ...,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        superclasses : typing.Optional[typing.Iterable[edgir.ref_pb2.LibraryPath]] = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"constraints",b"constraints",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"self_class",b"self_class",u"superclasses",b"superclasses"]) -> None: ...
global___Bundle = Bundle

class PortArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PortsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___PortLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___PortLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    SELF_CLASS_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    # The class that applies to every port in the set/array. Used
    #when a new port is instantiated by the front or back end.
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # Only designs should contain actual ports here
    @property
    def ports(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PortLike]: ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        ports : typing.Optional[typing.Mapping[typing.Text, global___PortLike]] = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"ports",b"ports",u"self_class",b"self_class"]) -> None: ...
global___PortArray = PortArray

#* Wrapper for different port like elements
class PortLike(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNDEFINED_FIELD_NUMBER: builtins.int
    LIB_ELEM_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    ARRAY_FIELD_NUMBER: builtins.int
    BUNDLE_FIELD_NUMBER: builtins.int
    @property
    def undefined(self) -> edgir.common_pb2.Empty: ...
    @property
    def lib_elem(self) -> edgir.ref_pb2.LibraryPath: ...
    #* 'port' disallowed w/in the library
    @property
    def port(self) -> global___Port: ...
    @property
    def array(self) -> global___PortArray: ...
    #* 'bundle' disallowed w/in the library
    @property
    def bundle(self) -> global___Bundle: ...
    def __init__(self,
        *,
        undefined : typing.Optional[edgir.common_pb2.Empty] = ...,
        lib_elem : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        port : typing.Optional[global___Port] = ...,
        array : typing.Optional[global___PortArray] = ...,
        bundle : typing.Optional[global___Bundle] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"array",b"array",u"bundle",b"bundle",u"is",b"is",u"lib_elem",b"lib_elem",u"port",b"port",u"undefined",b"undefined"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"array",b"array",u"bundle",b"bundle",u"is",b"is",u"lib_elem",b"lib_elem",u"port",b"port",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"is",b"is"]) -> typing.Optional[typing_extensions.Literal["undefined","lib_elem","port","array","bundle"]]: ...
global___PortLike = PortLike

class HierarchyBlock(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ParamsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.init_pb2.ValInit: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.init_pb2.ValInit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___PortLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___PortLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class BlocksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___BlockLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___BlockLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class LinksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___LinkLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___LinkLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.expr_pb2.ValueExpr: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.expr_pb2.ValueExpr] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class GeneratorsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___Generator: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___Generator] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    PARAMS_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    BLOCKS_FIELD_NUMBER: builtins.int
    LINKS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    SELF_CLASS_FIELD_NUMBER: builtins.int
    SUPERCLASSES_FIELD_NUMBER: builtins.int
    PREREFINE_CLASS_FIELD_NUMBER: builtins.int
    GENERATORS_FIELD_NUMBER: builtins.int
    IS_ABSTRACT_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.init_pb2.ValInit]: ...
    @property
    def ports(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PortLike]: ...
    #* Bridges, which adapt an edge port to a link port - eg, edge VoltageSink to an internal link
    #VoltageSource, are defined as blocks in the IR. Upper layers can define convenience constructs and/or
    #infer these blocks.
    @property
    def blocks(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___BlockLike]: ...
    @property
    def links(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___LinkLike]: ...
    #* Connections between internal block and link ports are represented by connected constraints.
    #Connections between internal; block and edge (of this block) ports are represented by exported constraints.
    @property
    def constraints(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.expr_pb2.ValueExpr]: ...
    # self class, equivalent to the library name
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # superclasses, may be empty
    @property
    def superclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]: ...
    # if refined: the class pre-refinement; otherwise equal to class
    @property
    def prerefine_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # optional, and removed upon invocation
    @property
    def generators(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___Generator]: ...
    # true if self_class is abstract, and should error if used in a design
    is_abstract: builtins.bool = ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        params : typing.Optional[typing.Mapping[typing.Text, edgir.init_pb2.ValInit]] = ...,
        ports : typing.Optional[typing.Mapping[typing.Text, global___PortLike]] = ...,
        blocks : typing.Optional[typing.Mapping[typing.Text, global___BlockLike]] = ...,
        links : typing.Optional[typing.Mapping[typing.Text, global___LinkLike]] = ...,
        constraints : typing.Optional[typing.Mapping[typing.Text, edgir.expr_pb2.ValueExpr]] = ...,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        superclasses : typing.Optional[typing.Iterable[edgir.ref_pb2.LibraryPath]] = ...,
        prerefine_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        generators : typing.Optional[typing.Mapping[typing.Text, global___Generator]] = ...,
        is_abstract : builtins.bool = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"prerefine_class",b"prerefine_class",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"blocks",b"blocks",u"constraints",b"constraints",u"generators",b"generators",u"is_abstract",b"is_abstract",u"links",b"links",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"prerefine_class",b"prerefine_class",u"self_class",b"self_class",u"superclasses",b"superclasses"]) -> None: ...
global___HierarchyBlock = HierarchyBlock

class Generator(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FN_FIELD_NUMBER: builtins.int
    REQUIRED_PARAMS_FIELD_NUMBER: builtins.int
    REQUIRED_PORTS_FIELD_NUMBER: builtins.int
    CONNECTED_BLOCKS_FIELD_NUMBER: builtins.int
    # Python function name for the generator. TODO dupe of the key in the containing map?
    fn: typing.Text = ...
    # Parameters that must be defined for the generator to fire.
    # These parameters are the only ones accessible to the generator.
    # TODO: perhaps should be a more general ValueExpr?
    @property
    def required_params(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LocalPath]: ...
    # Ports that must have defined connected-ness for the generator to fire.
    # This makes the port's IS_CONNECTED and CONNECTED_LINK.NAME available.
    @property
    def required_ports(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LocalPath]: ...
    # Internal blocks that this generator can (but not necessarily) make connections to.
    # TODO generalize to include all ports to allow appending connections?
    @property
    def connected_blocks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LocalPath]: ...
    def __init__(self,
        *,
        fn : typing.Text = ...,
        required_params : typing.Optional[typing.Iterable[edgir.ref_pb2.LocalPath]] = ...,
        required_ports : typing.Optional[typing.Iterable[edgir.ref_pb2.LocalPath]] = ...,
        connected_blocks : typing.Optional[typing.Iterable[edgir.ref_pb2.LocalPath]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connected_blocks",b"connected_blocks",u"fn",b"fn",u"required_params",b"required_params",u"required_ports",b"required_ports"]) -> None: ...
global___Generator = Generator

class BlockLike(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNDEFINED_FIELD_NUMBER: builtins.int
    LIB_ELEM_FIELD_NUMBER: builtins.int
    HIERARCHY_FIELD_NUMBER: builtins.int
    @property
    def undefined(self) -> edgir.common_pb2.Empty: ...
    @property
    def lib_elem(self) -> edgir.ref_pb2.LibraryPath: ...
    #* not allowed w/in the library
    @property
    def hierarchy(self) -> global___HierarchyBlock: ...
    def __init__(self,
        *,
        undefined : typing.Optional[edgir.common_pb2.Empty] = ...,
        lib_elem : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        hierarchy : typing.Optional[global___HierarchyBlock] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"hierarchy",b"hierarchy",u"lib_elem",b"lib_elem",u"type",b"type",u"undefined",b"undefined"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hierarchy",b"hierarchy",u"lib_elem",b"lib_elem",u"type",b"type",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"type",b"type"]) -> typing.Optional[typing_extensions.Literal["undefined","lib_elem","hierarchy"]]: ...
global___BlockLike = BlockLike

class Link(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ParamsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.init_pb2.ValInit: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.init_pb2.ValInit] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class PortsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___PortLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___PortLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class LinksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___LinkLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___LinkLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.expr_pb2.ValueExpr: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.expr_pb2.ValueExpr] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    PARAMS_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    LINKS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    SELF_CLASS_FIELD_NUMBER: builtins.int
    SUPERCLASSES_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.init_pb2.ValInit]: ...
    @property
    def ports(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PortLike]: ...
    @property
    def links(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___LinkLike]: ...
    @property
    def constraints(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.expr_pb2.ValueExpr]: ...
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # superclasses, may be empty
    @property
    def superclasses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[edgir.ref_pb2.LibraryPath]: ...
    # TODO: this provides type hierarchy data only, inheritance semantics are currently undefined

    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        params : typing.Optional[typing.Mapping[typing.Text, edgir.init_pb2.ValInit]] = ...,
        ports : typing.Optional[typing.Mapping[typing.Text, global___PortLike]] = ...,
        links : typing.Optional[typing.Mapping[typing.Text, global___LinkLike]] = ...,
        constraints : typing.Optional[typing.Mapping[typing.Text, edgir.expr_pb2.ValueExpr]] = ...,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        superclasses : typing.Optional[typing.Iterable[edgir.ref_pb2.LibraryPath]] = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"constraints",b"constraints",u"links",b"links",u"meta",b"meta",u"params",b"params",u"ports",b"ports",u"self_class",b"self_class",u"superclasses",b"superclasses"]) -> None: ...
global___Link = Link

class LinkArray(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PortsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___PortLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___PortLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class ConstraintsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> edgir.expr_pb2.ValueExpr: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[edgir.expr_pb2.ValueExpr] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class LinksEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___LinkLike: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___LinkLike] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    SELF_CLASS_FIELD_NUMBER: builtins.int
    PORTS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    LINKS_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    # The class that applies to every link in the set/array. Used
    #when a new link is instantiated by the front or back end.
    @property
    def self_class(self) -> edgir.ref_pb2.LibraryPath: ...
    # Only designs should contain an implementation here
    # the last index is the index of the link, the first indices (if any) are the indices of the corresponding port in the inner link
    @property
    def ports(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___PortLike]: ...
    # includes all exported constraints to map link ports to my ports
    @property
    def constraints(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, edgir.expr_pb2.ValueExpr]: ...
    @property
    def links(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___LinkLike]: ...
    @property
    def meta(self) -> edgir.common_pb2.Metadata: ...
    def __init__(self,
        *,
        self_class : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        ports : typing.Optional[typing.Mapping[typing.Text, global___PortLike]] = ...,
        constraints : typing.Optional[typing.Mapping[typing.Text, edgir.expr_pb2.ValueExpr]] = ...,
        links : typing.Optional[typing.Mapping[typing.Text, global___LinkLike]] = ...,
        meta : typing.Optional[edgir.common_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"meta",b"meta",u"self_class",b"self_class"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"constraints",b"constraints",u"links",b"links",u"meta",b"meta",u"ports",b"ports",u"self_class",b"self_class"]) -> None: ...
global___LinkArray = LinkArray

class LinkLike(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNDEFINED_FIELD_NUMBER: builtins.int
    LIB_ELEM_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    ARRAY_FIELD_NUMBER: builtins.int
    @property
    def undefined(self) -> edgir.common_pb2.Empty: ...
    @property
    def lib_elem(self) -> edgir.ref_pb2.LibraryPath: ...
    #* not allowed w/in the library
    @property
    def link(self) -> global___Link: ...
    @property
    def array(self) -> global___LinkArray: ...
    def __init__(self,
        *,
        undefined : typing.Optional[edgir.common_pb2.Empty] = ...,
        lib_elem : typing.Optional[edgir.ref_pb2.LibraryPath] = ...,
        link : typing.Optional[global___Link] = ...,
        array : typing.Optional[global___LinkArray] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"array",b"array",u"lib_elem",b"lib_elem",u"link",b"link",u"type",b"type",u"undefined",b"undefined"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"array",b"array",u"lib_elem",b"lib_elem",u"link",b"link",u"type",b"type",u"undefined",b"undefined"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"type",b"type"]) -> typing.Optional[typing_extensions.Literal["undefined","lib_elem","link","array"]]: ...
global___LinkLike = LinkLike