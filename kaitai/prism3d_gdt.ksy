meta:
  id: prism3d_gdt
  title: Prism3D map model format
  file-extension: gdt
  endian: le
  encoding: utf8

seq:
  - id: magic
    contents: "GEOM"
  - id: version
    type: str
    size: 4
  - id: num_models
    type: u4
  - id: models
    type: model
    repeat: expr
    repeat-expr: 13 # num_models

types:
  model:
    seq:
      - id: flags
        type: u4
      - id: block_s1
        type: s2
      - id: block_index
        type: s2
      - id: block_zero1
        type: u4
      - id: block_float1
        type: f4
      - id: block_float2
        type: f4
      - id: block_float3
        type: f4
      - id: block_float4
        type: f4
      - id: num_vertices
        type: u2
      - id: num_indices
        type: u2
      - id: indices
        type: u2
        repeat: expr
        repeat-expr: num_indices
      - id: vertices
        type: vector3f
        repeat: expr
        repeat-expr: num_vertices
      - id: colors
        type: u4
        repeat: expr
        repeat-expr: num_vertices
      - id: uvs
        type: uv
        repeat: expr
        repeat-expr: num_vertices
      - id: xyzr_5d
        type: f4
        repeat: expr
        repeat-expr: 4
        if: flags == 0x5d
      - id: extra_7d
        type: f4
        repeat: expr
        repeat-expr: 9
        if: flags == 0x7d

  uv:
    seq:
      - id: vector
        type: vector3f
        if: _parent.flags != 0x5d
      - id: u
        type: f4
      - id: v
        type: f4

  vector3f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
