# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class DarkstoneO3d(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.vertex_count = self._io.read_u4le()
        self.face_count = self._io.read_u4le()
        self.unknown1 = self._io.read_u4le()
        self.unknown2 = self._io.read_u4le()
        self.vertices = []
        for i in range(self.vertex_count):
            self.vertices.append(DarkstoneO3d.Vector3f(self._io, self, self._root))

        self.faces = []
        for i in range(self.face_count):
            self.faces.append(DarkstoneO3d.Face(self._io, self, self._root))


    class Bgra(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b = self._io.read_u1()
            self.g = self._io.read_u1()
            self.r = self._io.read_u1()
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


    class Face(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.color = DarkstoneO3d.Bgra(self._io, self, self._root)
            self.tex_coords = []
            for i in range(4):
                self.tex_coords.append(DarkstoneO3d.Vector2f(self._io, self, self._root))

            self.indices = []
            for i in range(4):
                self.indices.append(self._io.read_u2le())

            self.flags = self._io.read_u4le()
            self.tex_number = self._io.read_u2le()



