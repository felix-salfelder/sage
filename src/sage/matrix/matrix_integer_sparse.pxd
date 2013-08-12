include 'sage/ext/cdefs.pxi'
include 'sage/modules/vector_integer_sparse_h.pxi'

cdef extern from "sage/ext/multi_modular.h":
    ctypedef unsigned long mod_int

cimport matrix_sparse

cdef class Matrix_integer_sparse(matrix_sparse.Matrix_sparse):
    cdef mpz_vector* _matrix
    cdef int _initialized

    cdef _mod_int_c(self, mod_int p)
