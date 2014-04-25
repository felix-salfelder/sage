/*
Wrappers for malloc(), calloc(), free(), realloc().


AUTHORS:

- Jeroen Demeyer (2011-01-13): initial version (#10258)

*/

/*****************************************************************************
 *       Copyright (C) 2011 Jeroen Demeyer <jdemeyer@cage.ugent.be>
 *
 *  Distributed under the terms of the GNU General Public License (GPL)
 *  as published by the Free Software Foundation; either version 2 of
 *  the License, or (at your option) any later version.
 *                  http://www.gnu.org/licenses/
 ****************************************************************************/

#include "gmp_or_mpir.h"
#include "memory.h"

static void alloc_error(size_t size)
{
    PyGILState_STATE gilstate_save = PyGILState_Ensure();
    PyErr_Format(PyExc_MemoryError, "failed to allocate %zu bytes", size);
    PyGILState_Release(gilstate_save);
    sig_error();
}

/* mpir memory functions */
void* sage_mpir_malloc(size_t size)
{
    void* p = sage_malloc(size);
    if (unlikely(!p)) alloc_error(size);
    return p;
}

void* sage_mpir_realloc(void *ptr, size_t old_size, size_t new_size)
{
    void* p = sage_realloc(ptr, new_size);
    if (unlikely(!p)) alloc_error(new_size);
    return p;
}

void sage_mpir_free(void *ptr, size_t size)
{
    sage_free(ptr);
}

void init_memory_functions()
{
    mp_set_memory_functions(sage_mpir_malloc, sage_mpir_realloc, sage_mpir_free);
}
