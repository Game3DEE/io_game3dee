meta:
  id: canopygames_mdl
  title: Model format of older Canopy Games
  application: 'Harley Davidson: Race Across America'
  license: CC0
  file-extension: mdl
  endian: le
  encoding: utf8


seq:
  - id: num_elements
    type: u4
  - id: elements
    type: element
    repeat: expr
    repeat-expr: num_elements

types:
  element:
    seq:
    - id: len_type
      type: u4
    - id: type
      type: str
      size: len_type
    - id: len_name
      type: u4
    - id: name
      type: str
      size: len_name
    - id: num_attributes
      type: u4
    - id: attributes
      type: key_value
      repeat: expr
      repeat-expr: num_attributes

  key_value:
    seq:
      - id: index
        type: u4
      - id: type
        type: u4
        enum: value_type
      - id: len_key
        type: u4
      - id: key
        type: str
        size: len_key
      - id: value_size
        type: u4
      - id: value
        type:
          switch-on: type
          cases:
            value_type::signed_integer: s4
            value_type::unsigned_integer: u4
            value_type::texture_wrap: u4
            value_type::float: f4
            value_type::double: f8
            value_type::vector3f: vector3f
            value_type::rgba: rgba
            value_type::string: value_str(value_size)
            value_type::vertexmat: vertex_mat_data
            value_type::shadearray: shade_array_data
            value_type::texcoords: tex_coords_data
            value_type::vertex_table: vertex_table_data
            value_type::polyvertex: poly_vertex_data
            value_type::byte_table: byte_table_data
            value_type::poly_shader: poly_shader_data
            value_type::morph_keys: morph_keys_data

  morph_keys_data:
    seq:
      - id: len_morph_keys_buffer
        type: u4
      - id: num_morph_keys
        type: u4
      - id: morph_keys
        size: len_morph_keys_buffer
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  poly_shader_data:
    seq:
      - id: len_poly_shader_buffer
        type: u4
      - id: num_poly_shaders
        type: u4
      - id: poly_shaders
        type: u4
        repeat: expr
        repeat-expr: num_poly_shaders
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  byte_table_data:
    seq:
      - id: len_bytes
        type: u4
      - id: num_bytes
        type: u4
      - id: bytes
        size: len_bytes
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  vertex_mat_data:
    seq:
      - id: len_vertex_mat_buffer
        type: u4
      - id: num_vertex_mat
        type: u4
      - id: vertex_mat
        type: u4
        repeat: expr
        repeat-expr: num_vertex_mat
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  shade_array_data:
    seq:
      - id: len_shade_buffer
        type: u4
      - id: num_indices
        type: u4
      - id: indices
        type: u4
        repeat: expr
        repeat-expr: num_indices
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  tex_coords_data:
    seq:
      - id: len_uv_buffer
        type: u4
      - id: num_uvs
        type: u4
      - id: uvs
        type: vector2f
        repeat: expr
        repeat-expr: num_uvs
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  vertex_table_data:
    seq:
      - id: len_vertex_buffer
        type: u4
      - id: num_vertices
        type: u4
      - id: vertices
        type: vector3f
        repeat: expr
        repeat-expr: num_vertices
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  poly_vertex_data:
    seq:
      - id: len_index_buffer
        type: u4
      - id: num_polies
        type: u4
      - id: indices
        type: u4
        repeat: expr
        repeat-expr: len_index_buffer / 4
      - contents: [ 0xff, 0xff, 0xff, 0xff ]

  value_str:
    params:
      - id: len
        type: u4
    seq:
      - id: string
        type: str
        size: len

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

  rgba:
    seq:
      - id: r
        type: f4
      - id: g
        type: f4
      - id: b
        type: f4
      - id: a
        type: f4

enums:
  value_type:
    1: signed_integer
    4: unsigned_integer
    7: texture_wrap
    8: float
    9: double
    11: vector3f
    12: rgba
    16: string
    104: vertexmat
    107: shadearray
    110: texcoords
    111: vertex_table
    114: polyvertex
    105: byte_table
    1001: poly_shader
    1003: morph_keys
