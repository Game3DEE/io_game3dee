meta:
  id: prism3d_pmd
  title: Prism3D Modal format
  file-extension: pmd
  endian: le
  encoding: utf8

seq:
  - id: version
    type: u4

  - id: num_objects
    type: u4

  - id: object_headers
    type: object_header
    repeat: expr
    repeat-expr: max_objects

  - id: num_morph_targets
    type: u4
  - id: num_animations
    type: u4

  - id: bbox_min
    type: vector3f
  - id: bbox_max
    type: vector3f
  - id: scale
    type: vector3f

  - id: zeroes
    size: 192

  - id: animation_headers
    type: animation_header
    repeat: expr
    repeat-expr: max_animations

  - id: objects
    type: obj(_index)
    repeat: expr
    repeat-expr: num_objects

  - id: animations
    type: animation(_index)
    repeat: expr
    repeat-expr: num_animations

instances:
  max_objects:
    value: 16
  max_animations:
    value: 64

types:
  animation_header:
    seq:
      - id: num_frames
        type: u4
      - id: fps
        type: f4
      - id: duration
        type: f4
      - id: name
        type: strz
        size: 32
      - id: val1
        type: u4
      - id: val2
        type: u4

  obj:
    params:
      - id: index
        type: u4
    seq:
      - id: indices
        type: u2
        repeat: expr
        repeat-expr: num_indices
      - id: vertices
        type: vector3i
        repeat: expr
        repeat-expr: num_vertices * _root.num_morph_targets
      - id: uvs
        type: vector2f
        repeat: expr
        repeat-expr: num_vertices
    instances:
      num_indices:
        value: _root.object_headers[index].num_triangles * 3
      num_vertices:
        value: _root.object_headers[index].num_vertices

  object_header:
    seq:
      - id: name
        type: strz
        size: 16
      - id: num_triangles
        type: u4
      - id: num_vertices
        type: u4
      - id: val1
        type: u4

  animation:
    params:
      - id: index
        type: u4
    seq:
      - id: indices
        type: u4
        repeat: expr
        repeat-expr: num_frames
      - id: weights
        type: f4
        repeat: expr
        repeat-expr: num_frames
    instances:
      num_frames:
        value: _root.animation_headers[index].num_frames

  vector3i:
    seq:
      - id: x
        type: s2
      - id: y
        type: s2
      - id: z
        type: s2
      - id: index
        type: u1

  vector3f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  vector2f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
