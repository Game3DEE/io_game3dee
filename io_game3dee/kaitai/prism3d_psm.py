# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Prism3dPsm(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_u4le()
        self.num_locators = self._io.read_u4le()
        self.num_objects = self._io.read_u4le()
        if self.version > 3:
            self.unknown = self._io.read_u4le()

        self.locators = []
        for i in range(self.num_locators):
            self.locators.append(Prism3dPsm.Locator(self._io, self, self._root))

        self.objects = []
        for i in range(self.num_objects):
            self.objects.append(Prism3dPsm.Obj(self._io, self, self._root))


    class Vector4f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.w = self._io.read_f4le()


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
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"utf8")
            self.num_triangles = self._io.read_u4le()
            self.num_vertices = self._io.read_u4le()
            self.matrix_index = self._io.read_u4le()
            self.unknown_1 = self._io.read_u4le()
            self.unknown_2 = self._io.read_u4le()
            self.unknown_3 = self._io.read_bytes(16)
            self.vertices = []
            for i in range(self.num_vertices):
                self.vertices.append(Prism3dPsm.Vector3f(self._io, self, self._root))

            self.unk2a = self._io.read_bytes((self.unknown_2 * self.num_vertices))
            self.unk2b = []
            for i in range((self.unknown_2 * self.num_vertices)):
                self.unk2b.append(self._io.read_f4le())

            self.normals = []
            for i in range(self.num_vertices):
                self.normals.append(Prism3dPsm.Vector3f(self._io, self, self._root))

            if self.unknown_1 == 3:
                self.unknown = []
                for i in range(self.num_vertices):
                    self.unknown.append(self._io.read_f4le())


            self.uvs = []
            for i in range(self.num_vertices):
                self.uvs.append(Prism3dPsm.Vector2f(self._io, self, self._root))

            self.indices = []
            for i in range((self.num_triangles * 3)):
                self.indices.append(self._io.read_s2le())

            if self._root.version > 3:
                self.face_indices_2 = []
                for i in range(self.num_triangles):
                    self.face_indices_2.append(self._io.read_u2le())




    class Matrix(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rot1 = Prism3dPsm.Vector4f(self._io, self, self._root)
            self.pos1 = Prism3dPsm.Vector3f(self._io, self, self._root)
            self.pos2 = Prism3dPsm.Vector3f(self._io, self, self._root)
            self.rot2 = Prism3dPsm.Vector4f(self._io, self, self._root)


    class Vector2f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()


    class Locator(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u4le()
            self.matrices = []
            for i in range(self.count):
                self.matrices.append(Prism3dPsm.Matrix(self._io, self, self._root))

            self.indices = []
            for i in range(self.count):
                self.indices.append(self._io.read_s1())

            self.weights = []
            for i in range(self.count):
                self.weights.append(self._io.read_f4le())

            self.names = []
            for i in range(self.count):
                self.names.append((KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"utf8"))




