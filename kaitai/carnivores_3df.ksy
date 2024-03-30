meta:
  id: carnivores_3df
  title: Model format of Carnivores 1/2/Ice Age (for PC)
  file-extension: 3df
  endian: le
  encoding: utf8
  license: CC0

seq:
  - id: num_vertices
    type: u4
  - id: num_faces
    type: u4
  - id: num_bones
    type: u4
  - id: len_texture
    type: u4
  - id: faces
    type: face
    repeat: expr
    repeat-expr: num_faces
  - id: vertices
    type: vertex
    repeat: expr
    repeat-expr: num_vertices
  - id: bones
    type: bone
    repeat: expr
    repeat-expr: num_bones
  - id: texture
    size: len_texture
    if: (_io.size - _io.pos) >= len_texture
    doc: |
      Texture data in BGRA5551 format. Texture width is fixed to 256, so height
      can be calculated as (len_texture / 256) / 2.

types:
  face:
    seq:
      - id: indices
        type: u4
        repeat: expr
        repeat-expr: 3
        doc: Vertex indices to define the triangle for this face
      - id: u
        type: u4
        repeat: expr
        repeat-expr: 3
        doc: integer texture coordinate U for all three vertices
      - id: v
        type: u4
        repeat: expr
        repeat-expr: 3
        doc: integer texture coordinate V for all three vertices
      - id: flags
        type: u2
      - id: dmask
        type: u2
        doc: Unused by games; maybe used by tooling?
      - id: distant
        type: u4
        doc: Unused
      - id: next
        type: s4
        doc: Used during game for sorting faces
      - id: group
        type: u4
        doc: Unused by games; maybe used by tooling?
      - id: reserved
        size: 12
        doc: Unused; reserved for future usage

  vertex:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: bone_index
        type: u2
        doc: index of bone this vertex belongs too.
      - id: hidden
        type: u2
        doc: Used in tooling to store wether this vertex is visible. Unused in game.

  bone:
    seq:
      - id: name
        type: strz
        size: 32
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: parent
        type: s2
        doc: index of parent bone, or -1 if unattached.
      - id: hidden
        type: u2
        doc: Used in tooling to store wether this bone is visible. Unused in game.
