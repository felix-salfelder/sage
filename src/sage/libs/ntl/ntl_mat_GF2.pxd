include "decl.pxi"
include "sage/ext/cdefs.pxi"

from ntl_GF2 cimport ntl_GF2

cdef class ntl_mat_GF2:
    cdef mat_GF2_c x
    cdef ntl_GF2 _new_element(self)
    cdef ntl_mat_GF2 _new(self)
