meta:
  id: prism3d_psm
  title: Prism3D psm model format
  file-extension: psm
  endian: le
  encoding: utf8

seq:
  - id: version
    type: u4
  - id: num_locators
    type: u4
  - id: num_objects
    type: u4
  - id: unknown
    type: u4
    if: version > 3
  - id: locators
    type: locator
    repeat: expr
    repeat-expr: num_locators
  - id: objects
    type: obj
    repeat: expr
    repeat-expr: num_objects

types:
  obj:
    seq:
      - id: name
        type: strz
        size: 16
      - id: num_triangles
        type: u4
      - id: num_vertices
        type: u4
      - id: matrix_index
        type: u4
      - id: unknown_1
        type: u4
      - id: unknown_2
        type: u4
      - id: unknown_3
        size: 16
      - id: vertices
        type: vector3f
        repeat: expr
        repeat-expr: num_vertices
      - id: unk2a
        size: unknown_2 * num_vertices
      - id: unk2b
        type: f4
        repeat: expr
        repeat-expr: unknown_2 * num_vertices
      - id: normals
        type: vector3f
        repeat: expr
        repeat-expr: num_vertices
      - id: unknown
        type: f4
        repeat: expr
        repeat-expr: num_vertices
        if: unknown_1 == 3
      - id: uvs
        type: vector2f
        repeat: expr
        repeat-expr: num_vertices
      - id: indices
        type: s2
        repeat: expr
        repeat-expr: num_triangles * 3
      - id: face_indices_2
        type: u2
        repeat: expr
        repeat-expr: num_triangles
        if: _root.version > 3

  locator:
    seq:
      - id: count
        type: u4
      - id: matrices
        type: matrix
        repeat: expr
        repeat-expr: count
      - id: indices
        type: s1
        repeat: expr
        repeat-expr: count
      - id: weights
        type: f4
        repeat: expr
        repeat-expr: count
      - id: names
        type: strz
        size: 16
        repeat: expr
        repeat-expr: count

  matrix:
    seq:
      - id: rot1
        type: vector4f
      - id: pos1
        type: vector3f
      - id: pos2
        type: vector3f
      - id: rot2
        type: vector4f

  vector2f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4

  vector3f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4

  vector4f:
    seq:
    - id: x
      type: f4
    - id: y
      type: f4
    - id: z
      type: f4
    - id: w
      type: f4
