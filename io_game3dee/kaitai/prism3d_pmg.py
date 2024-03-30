# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Prism3dPmg(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_u1()
        self.magic = self._io.read_bytes(3)
        if not self.magic == b"\x67\x6D\x50":
            raise kaitaistruct.ValidationNotEqualError(b"\x67\x6D\x50", self.magic, self._io, u"/seq/1")
        self.num_objects = self._io.read_u4le()
        self.count_1 = self._io.read_u4le()
        self.count_2 = self._io.read_u4le()
        self.count_3 = self._io.read_u4le()
        self.center = Prism3dPmg.Vector3f(self._io, self, self._root)
        self.radius = self._io.read_f4le()
        if self._root.version > 16:
            self.floats = []
            for i in range(6):
                self.floats.append(self._io.read_f4le())


        self.data_offset_1 = self._io.read_u4le()
        self.data_offset_2 = self._io.read_u4le()
        self.data_offset_3 = self._io.read_u4le()
        self.data_offset_4 = self._io.read_u4le()
        self.data_offset_5 = self._io.read_u4le()
        self.data_size_1 = self._io.read_u4le()
        self.data_offset_7 = self._io.read_u4le()
        self.data_size_2 = self._io.read_u4le()
        self.data_offset_9 = self._io.read_u4le()
        self.data_offset_10 = self._io.read_u4le()
        self.data_offset_11 = self._io.read_u4le()
        self.data_size_3 = self._io.read_u4le()
        self.data_offset_13 = self._io.read_u4le()
        self.data_size_4 = self._io.read_u4le()
        self.unknown_data_1 = []
        for i in range((self.count_1 * 6)):
            self.unknown_data_1.append(self._io.read_u4le())

        self.unknown_data_2 = []
        for i in range(self.count_3):
            self.unknown_data_2.append(Prism3dPmg.Unknown2(self._io, self, self._root))


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


    class Obj(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_indices = self._io.read_u4le()
            self.num_vertices = self._io.read_u4le()
            self.val1 = self._io.read_u4le()
            self.index = self._io.read_u4le()
            self.center = Prism3dPmg.Vector3f(self._io, self, self._root)
            self.radius = self._io.read_f4le()
            if self._root.version > 16:
                self.floats = []
                for i in range(6):
                    self.floats.append(self._io.read_f4le())


            self.vertex_data_offset = self._io.read_s4le()
            self.normal_data_offset = self._io.read_s4le()
            self.uv_data_offset = self._io.read_s4le()
            self.colors_data_offset = self._io.read_s4le()
            self.data_offset_1 = self._io.read_s4le()
            self.data_offset_2 = self._io.read_s4le()
            self.index_data_offset = self._io.read_s4le()
            self.data_offset_3 = self._io.read_s4le()
            self.data_offset_4 = self._io.read_s4le()
            self.data_offset_5 = self._io.read_s4le()

        @property
        def indices(self):
            if hasattr(self, '_m_indices'):
                return self._m_indices

            if self.index_data_offset != -1:
                _pos = self._io.pos()
                self._io.seek(self.index_data_offset)
                self._m_indices = []
                for i in range(self.num_indices):
                    self._m_indices.append(self._io.read_u2le())

                self._io.seek(_pos)

            return getattr(self, '_m_indices', None)

        @property
        def vertices(self):
            if hasattr(self, '_m_vertices'):
                return self._m_vertices

            if self.vertex_data_offset != -1:
                _pos = self._io.pos()
                self._io.seek(self.vertex_data_offset)
                self._m_vertices = []
                for i in range(self.num_vertices):
                    self._m_vertices.append(Prism3dPmg.Vector3f(self._io, self, self._root))

                self._io.seek(_pos)

            return getattr(self, '_m_vertices', None)

        @property
        def uvs(self):
            if hasattr(self, '_m_uvs'):
                return self._m_uvs

            if self.uv_data_offset != -1:
                _pos = self._io.pos()
                self._io.seek(self.uv_data_offset)
                self._m_uvs = []
                for i in range(self.num_vertices):
                    self._m_uvs.append(Prism3dPmg.Vector2f(self._io, self, self._root))

                self._io.seek(_pos)

            return getattr(self, '_m_uvs', None)

        @property
        def colors(self):
            if hasattr(self, '_m_colors'):
                return self._m_colors

            if self.colors_data_offset != -1:
                _pos = self._io.pos()
                self._io.seek(self.colors_data_offset)
                self._m_colors = []
                for i in range(self.num_vertices):
                    self._m_colors.append(Prism3dPmg.Color4b(self._io, self, self._root))

                self._io.seek(_pos)

            return getattr(self, '_m_colors', None)

        @property
        def normals(self):
            if hasattr(self, '_m_normals'):
                return self._m_normals

            if self.normal_data_offset != -1:
                _pos = self._io.pos()
                self._io.seek(self.normal_data_offset)
                self._m_normals = []
                for i in range(self.num_vertices):
                    self._m_normals.append(Prism3dPmg.Vector3f(self._io, self, self._root))

                self._io.seek(_pos)

            return getattr(self, '_m_normals', None)


    class Unknown2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.val1 = self._io.read_u4le()
            self.val2 = self._io.read_u4le()
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.r = self._io.read_f4le()
            self.x2 = self._io.read_f4le()
            self.y2 = self._io.read_f4le()
            self.z2 = self._io.read_f4le()
            self.r2 = self._io.read_f4le()


    class Color4b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()
            self.a = self._io.read_u1()


    class Vector2f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()


    @property
    def objects(self):
        if hasattr(self, '_m_objects'):
            return self._m_objects

        _pos = self._io.pos()
        self._io.seek(self.data_offset_3)
        self._m_objects = []
        for i in range(self.num_objects):
            self._m_objects.append(Prism3dPmg.Obj(self._io, self, self._root))

        self._io.seek(_pos)
        return getattr(self, '_m_objects', None)


