# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Quickdraw3d3dmf(KaitaiStruct):

    class PixelType(Enum):
        rgb32 = 0
        argb32 = 1
        rgb16 = 2
        argb16 = 3
        rgb16_565 = 4
        rgb24 = 5
        unknown = 200

    class AttributeType(Enum):
        none = 0
        surface_uv = 1
        shading_uv = 2
        normal = 3
        ambient_coefficient = 4
        diffuse_color = 5
        specular_color = 6
        specular_control = 7
        transparency_color = 8
        surface_tangent = 9
        highlight_state = 10
        surface_shader = 11
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x33\x44\x4D\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x33\x44\x4D\x46", self.magic, self._io, u"/seq/0")
        self.header_length = self._io.read_bytes(4)
        if not self.header_length == b"\x00\x00\x00\x10":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x10", self.header_length, self._io, u"/seq/1")
        self.version_major = self._io.read_u2be()
        self.version_minor = self._io.read_u2be()
        self.flags = self._io.read_bytes(4)
        if not self.flags == b"\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.flags, self._io, u"/seq/4")
        self.toc_offset = self._io.read_u8be()
        self.chunks = []
        i = 0
        while not self._io.is_eof():
            self.chunks.append(Quickdraw3d3dmf.Chunk(self._io, self, self._root))
            i += 1


    class Chunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = (self._io.read_bytes(4)).decode(u"utf8")
            self.size = self._io.read_u4be()
            _on = self.type
            if _on == u"bgng":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.ChunkList(_io__raw_data, self, self._root)
            elif _on == u"atar":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.AtarData(_io__raw_data, self, self._root)
            elif _on == u"txpm":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.TxpmData(_io__raw_data, self, self._root)
            elif _on == u"kxpr":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.Color3f(_io__raw_data, self, self._root)
            elif _on == u"txmm":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.TxmmData(_io__raw_data, self, self._root)
            elif _on == u"kdif":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.Color3f(_io__raw_data, self, self._root)
            elif _on == u"cntr":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.ChunkList(_io__raw_data, self, self._root)
            elif _on == u"shdr":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.ShdrData(_io__raw_data, self, self._root)
            elif _on == u"rfrn":
                self.data = self._io.read_u4be()
            elif _on == u"tmsh":
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Quickdraw3d3dmf.TrimeshData(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.size)


    class TxmmData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.use_mipmapping = self._io.read_u4be()
            self.pixel_type = KaitaiStream.resolve_enum(Quickdraw3d3dmf.PixelType, self._io.read_u4be())
            self.bit_order = self._io.read_u4be()
            self.byte_order = self._io.read_u4be()
            self.width = self._io.read_u4be()
            self.height = self._io.read_u4be()
            self.row_bytes = self._io.read_u4be()


    class TxpmData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.width = self._io.read_u4be()
            self.height = self._io.read_u4be()
            self.row_bytes = self._io.read_u4be()
            self.pixel_size = self._io.read_u4be()
            self.pixel_type = KaitaiStream.resolve_enum(Quickdraw3d3dmf.PixelType, self._io.read_u4be())
            self.bit_order = self._io.read_u4be()
            self.byte_order = self._io.read_u4be()


    class Vector3f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4be()
            self.y = self._io.read_f4be()
            self.z = self._io.read_f4be()


    class ShdrData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.boundary_u = self._io.read_u4be()
            self.boundary_v = self._io.read_u4be()


    class TrimeshData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_triangles = self._io.read_u4be()
            self.triangle_attribute_count = self._io.read_u4be()
            self.num_edges = self._io.read_u4be()
            self.edge_attribute_count = self._io.read_u4be()
            self.num_vertices = self._io.read_u4be()
            self.num_vertex_attributes = self._io.read_u4be()
            self.triangles = []
            for i in range((self.num_triangles * 3)):
                _on = self.index_size
                if _on == 1:
                    self.triangles.append(self._io.read_u1())
                elif _on == 2:
                    self.triangles.append(self._io.read_u2be())

            self.vertices = []
            for i in range(self.num_vertices):
                self.vertices.append(Quickdraw3d3dmf.Vector3f(self._io, self, self._root))

            self.bbox_min = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)
            self.bbox_max = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)

        @property
        def index_size(self):
            if hasattr(self, '_m_index_size'):
                return self._m_index_size

            self._m_index_size = (2 if self.num_vertices > 255 else 1)
            return getattr(self, '_m_index_size', None)


    class Tangent2v(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.u_tangent = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)
            self.v_tangent = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)


    class AtarData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.attribute_type = KaitaiStream.resolve_enum(Quickdraw3d3dmf.AttributeType, self._io.read_u4be())
            self.zero = self._io.read_bytes(4)
            if not self.zero == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.zero, self._io, u"/types/atar_data/seq/1")
            self.position_of_array = self._io.read_u4be()
            self.position_in_array = self._io.read_u4be()
            self.attribute_use_flag = self._io.read_u4be()
            _on = self.attribute_type
            if _on == Quickdraw3d3dmf.AttributeType.surface_uv:
                self.values = Quickdraw3d3dmf.Vector2f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.normal:
                self.values = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.diffuse_color:
                self.values = Quickdraw3d3dmf.Color4f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.transparency_color:
                self.values = Quickdraw3d3dmf.Vector3f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.surface_tangent:
                self.values = Quickdraw3d3dmf.Tangent2v(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.highlight_state:
                self.values = self._io.read_u4be()
            elif _on == Quickdraw3d3dmf.AttributeType.ambient_coefficient:
                self.values = self._io.read_f4be()
            elif _on == Quickdraw3d3dmf.AttributeType.specular_control:
                self.values = self._io.read_f4be()
            elif _on == Quickdraw3d3dmf.AttributeType.shading_uv:
                self.values = Quickdraw3d3dmf.Vector2f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.specular_color:
                self.values = Quickdraw3d3dmf.Color4f(self._io, self, self._root)
            elif _on == Quickdraw3d3dmf.AttributeType.surface_shader:
                self.values = self._io.read_u4be()


    class Color4f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_f4be()
            self.g = self._io.read_f4be()
            self.b = self._io.read_f4be()
            self.a = self._io.read_f4be()


    class Toc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.toc_magic = self._io.read_bytes(4)
            if not self.toc_magic == b"\x74\x6F\x63\x20":
                raise kaitaistruct.ValidationNotEqualError(b"\x74\x6F\x63\x20", self.toc_magic, self._io, u"/types/toc/seq/0")
            self.toc_size = self._io.read_u4be()
            self.next_toc = self._io.read_u8be()
            self.ref_seed = self._io.read_u4be()
            self.type_seed = self._io.read_u4be()
            self.toc_entry_type = self._io.read_bytes(4)
            if not self.toc_entry_type == b"\x00\x00\x00\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x01", self.toc_entry_type, self._io, u"/types/toc/seq/5")
            self.toc_entry_size = self._io.read_bytes(4)
            if not self.toc_entry_size == b"\x00\x00\x00\x10":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x10", self.toc_entry_size, self._io, u"/types/toc/seq/6")
            self.num_entries = self._io.read_u4be()
            self.entries = []
            for i in range(self.num_entries):
                self.entries.append(Quickdraw3d3dmf.TocEntry(self._io, self, self._root))



    class Vector2f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4be()
            self.y = self._io.read_f4be()


    class ChunkList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self.chunks.append(Quickdraw3d3dmf.Chunk(self._io, self, self._root))
                i += 1



    class Color3f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_f4be()
            self.g = self._io.read_f4be()
            self.b = self._io.read_f4be()


    class TocEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ref_id = self._io.read_u4be()
            self.obj_location = self._io.read_u8be()
            self.type = (self._io.read_bytes(4)).decode(u"utf8")


    @property
    def toc(self):
        if hasattr(self, '_m_toc'):
            return self._m_toc

        if self.toc_offset != 0:
            _pos = self._io.pos()
            self._io.seek(self.toc_offset)
            self._m_toc = Quickdraw3d3dmf.Toc(self._io, self, self._root)
            self._io.seek(_pos)

        return getattr(self, '_m_toc', None)


