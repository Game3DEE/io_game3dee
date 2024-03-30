# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CanopygamesMdl(KaitaiStruct):

    class ValueType(Enum):
        signed_integer = 1
        unsigned_integer = 4
        texture_wrap = 7
        float = 8
        double = 9
        vector3f = 11
        rgba = 12
        string = 16
        vertexmat = 104
        byte_table = 105
        shadearray = 107
        texcoords = 110
        vertex_table = 111
        polyvertex = 114
        poly_shader = 1001
        morph_keys = 1003
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.num_elements = self._io.read_u4le()
        self.elements = []
        for i in range(self.num_elements):
            self.elements.append(CanopygamesMdl.Element(self._io, self, self._root))


    class ByteTableData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_bytes = self._io.read_u4le()
            self.num_bytes = self._io.read_u4le()
            self.bytes = self._io.read_bytes(self.len_bytes)
            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/byte_table_data/seq/3")


    class ShadeArrayData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_shade_buffer = self._io.read_u4le()
            self.num_indices = self._io.read_u4le()
            self.indices = []
            for i in range(self.num_indices):
                self.indices.append(self._io.read_u4le())

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/shade_array_data/seq/3")


    class Vector3f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class Rgba(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_f4le()
            self.g = self._io.read_f4le()
            self.b = self._io.read_f4le()
            self.a = self._io.read_f4le()


    class VertexTableData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_vertex_buffer = self._io.read_u4le()
            self.num_vertices = self._io.read_u4le()
            self.vertices = []
            for i in range(self.num_vertices):
                self.vertices.append(CanopygamesMdl.Vector3f(self._io, self, self._root))

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/vertex_table_data/seq/3")


    class Element(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_type = self._io.read_u4le()
            self.type = (self._io.read_bytes(self.len_type)).decode(u"utf8")
            self.len_name = self._io.read_u4le()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"utf8")
            self.num_attributes = self._io.read_u4le()
            self.attributes = []
            for i in range(self.num_attributes):
                self.attributes.append(CanopygamesMdl.KeyValue(self._io, self, self._root))



    class VertexMatData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_vertex_mat_buffer = self._io.read_u4le()
            self.num_vertex_mat = self._io.read_u4le()
            self.vertex_mat = []
            for i in range(self.num_vertex_mat):
                self.vertex_mat.append(self._io.read_u4le())

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/vertex_mat_data/seq/3")


    class TexCoordsData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_uv_buffer = self._io.read_u4le()
            self.num_uvs = self._io.read_u4le()
            self.uvs = []
            for i in range(self.num_uvs):
                self.uvs.append(CanopygamesMdl.Vector2f(self._io, self, self._root))

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/tex_coords_data/seq/3")


    class KeyValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = self._io.read_u4le()
            self.type = KaitaiStream.resolve_enum(CanopygamesMdl.ValueType, self._io.read_u4le())
            self.len_key = self._io.read_u4le()
            self.key = (self._io.read_bytes(self.len_key)).decode(u"utf8")
            self.value_size = self._io.read_u4le()
            _on = self.type
            if _on == CanopygamesMdl.ValueType.polyvertex:
                self.value = CanopygamesMdl.PolyVertexData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.signed_integer:
                self.value = self._io.read_s4le()
            elif _on == CanopygamesMdl.ValueType.texture_wrap:
                self.value = self._io.read_u4le()
            elif _on == CanopygamesMdl.ValueType.vector3f:
                self.value = CanopygamesMdl.Vector3f(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.morph_keys:
                self.value = CanopygamesMdl.MorphKeysData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.float:
                self.value = self._io.read_f4le()
            elif _on == CanopygamesMdl.ValueType.rgba:
                self.value = CanopygamesMdl.Rgba(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.double:
                self.value = self._io.read_f8le()
            elif _on == CanopygamesMdl.ValueType.vertex_table:
                self.value = CanopygamesMdl.VertexTableData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.poly_shader:
                self.value = CanopygamesMdl.PolyShaderData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.vertexmat:
                self.value = CanopygamesMdl.VertexMatData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.shadearray:
                self.value = CanopygamesMdl.ShadeArrayData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.byte_table:
                self.value = CanopygamesMdl.ByteTableData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.unsigned_integer:
                self.value = self._io.read_u4le()
            elif _on == CanopygamesMdl.ValueType.texcoords:
                self.value = CanopygamesMdl.TexCoordsData(self._io, self, self._root)
            elif _on == CanopygamesMdl.ValueType.string:
                self.value = CanopygamesMdl.ValueStr(self.value_size, self._io, self, self._root)


    class ValueStr(KaitaiStruct):
        def __init__(self, len, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.len = len
            self._read()

        def _read(self):
            self.string = (self._io.read_bytes(self.len)).decode(u"utf8")


    class PolyShaderData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_poly_shader_buffer = self._io.read_u4le()
            self.num_poly_shaders = self._io.read_u4le()
            self.poly_shaders = []
            for i in range(self.num_poly_shaders):
                self.poly_shaders.append(self._io.read_u4le())

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/poly_shader_data/seq/3")


    class PolyVertexData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_index_buffer = self._io.read_u4le()
            self.num_polies = self._io.read_u4le()
            self.indices = []
            for i in range(self.len_index_buffer // 4):
                self.indices.append(self._io.read_u4le())

            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/poly_vertex_data/seq/3")


    class MorphKeysData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_morph_keys_buffer = self._io.read_u4le()
            self.num_morph_keys = self._io.read_u4le()
            self.morph_keys = self._io.read_bytes(self.len_morph_keys_buffer)
            self._unnamed3 = self._io.read_bytes(4)
            if not self._unnamed3 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self._unnamed3, self._io, u"/types/morph_keys_data/seq/3")


    class Vector2f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()



