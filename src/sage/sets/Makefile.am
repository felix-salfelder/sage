# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    all.py \
    cartesian_product.py \
    disjoint_union_enumerated_sets.py \
    family.py \
    finite_enumerated_set.py \
    finite_set_maps.py \
    __init__.py \
    integer_range.py \
    non_negative_integers.py \
    positive_integers.py \
    primes.py \
    real_set.py \
    set_from_iterator.py \
    set.py \
    totally_ordered_finite_set.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = \
    disjoint_set.la \
    finite_set_map_cy.la \
    recursively_enumerated_set.la

finite_set_map_cy_la_LIBADD = @CSAGE_LIBS@

disjoint_set_la_LIBADD = @GMP_OR_MPIR_LIBS@ -lflint @CSAGE_LIBS@
disjoint_set_la_CFLAGS = -std=c99 $(AM_CFLAGS)
disjoint_set_la_CPPFLAGS = -I@top_builddir@/libs/gap $(AM_CPPFLAGS)

noinst_HEADERS = recursively_enumerated_set.pxd
