# Autogenerated and manually edited file; see README.md for more details
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Prism3dPmd(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_u4le()
        self.num_objects = self._io.read_u4le()
        self.object_headers = []
        for i in range(self.max_objects):
            self.object_headers.append(Prism3dPmd.ObjectHeader(self._io, self, self._root))

        self.num_morph_targets = self._io.read_u4le()
        self.num_animations = self._io.read_u4le()
        self.bbox_min = Prism3dPmd.Vector3f(self._io, self, self._root)
        self.bbox_max = Prism3dPmd.Vector3f(self._io, self, self._root)
        self.scale = Prism3dPmd.Vector3f(self._io, self, self._root)
        self.zeroes = self._io.read_bytes(192)
        self.animation_headers = []
        for i in range(self.max_animations):
            self.animation_headers.append(Prism3dPmd.AnimationHeader(self._io, self, self._root))

        self.objects = []
        for i in range(self.num_objects):
            self.objects.append(Prism3dPmd.Obj(i, self._io, self, self._root))

        self.animations = []
        for i in range(self.num_animations):
            self.animations.append(Prism3dPmd.Animation(i, self._io, self, self._root))


    class Vector3i(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.z = self._io.read_s2le()
            self.index = self._io.read_u1()


    class ObjectHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"utf8")
            self.num_triangles = self._io.read_u4le()
            self.num_vertices = self._io.read_u4le()
            self.val1 = self._io.read_u4le()


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
        def __init__(self, index, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.index = index
            self._read()

        def _read(self):
            self.indices = []
            for i in range(self.num_indices):
                self.indices.append(self._io.read_u2le())

            self.vertices = []
            for i in range((self.num_vertices * self._root.num_morph_targets)):
                self.vertices.append(Prism3dPmd.Vector3i(self._io, self, self._root))

            self.uvs = []
            for i in range(self.num_vertices):
                self.uvs.append(Prism3dPmd.Vector2f(self._io, self, self._root))


        @property
        def num_indices(self):
            if hasattr(self, '_m_num_indices'):
                return self._m_num_indices

            self._m_num_indices = (self._root.object_headers[self.index].num_triangles * 3)
            return getattr(self, '_m_num_indices', None)

        @property
        def num_vertices(self):
            if hasattr(self, '_m_num_vertices'):
                return self._m_num_vertices

            self._m_num_vertices = self._root.object_headers[self.index].num_vertices
            return getattr(self, '_m_num_vertices', None)


    class Animation(KaitaiStruct):
        def __init__(self, index, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.index = index
            self._read()

        def _read(self):
            self.indices = []
            for i in range(self.num_frames):
                self.indices.append(self._io.read_u4le())

            self.weights = []
            for i in range(self.num_frames):
                self.weights.append(self._io.read_f4le())


        @property
        def num_frames(self):
            if hasattr(self, '_m_num_frames'):
                return self._m_num_frames

            self._m_num_frames = self._root.animation_headers[self.index].num_frames
            return getattr(self, '_m_num_frames', None)


    class Vector2f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()


    class AnimationHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_frames = self._io.read_u4le()
            self.fps = self._io.read_f4le()
            self.duration = self._io.read_f4le()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"utf8")
            self.val1 = self._io.read_u4le()
            self.val2 = self._io.read_u4le()


    @property
    def max_objects(self):
        if hasattr(self, '_m_max_objects'):
            return self._m_max_objects

        self._m_max_objects = 16
        return getattr(self, '_m_max_objects', None)

    @property
    def max_animations(self):
        if hasattr(self, '_m_max_animations'):
            return self._m_max_animations

        self._m_max_animations = 64
        return getattr(self, '_m_max_animations', None)


