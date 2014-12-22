# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    all.py \
    bibd.py \
    block_design.py \
    covering_design.py \
    database.py \
    design_catalog.py \
    difference_family.py \
    ext_rep.py \
    incidence_structures.py \
    __init__.py \
    latin_squares.py \
    orthogonal_arrays.py \
    orthogonal_arrays_recursive.py \
    steiner_quadruple_systems.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = designs_pyx.la
designs_pyx_la_LIBADD = $(CSAGE_LIBS)
