# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
setsdir = $(pythondir)/sage/sets
sets_PYTHON = \
    family.py __init__.py set.py finite_set_maps.py non_negative_integers.py \
    disjoint_union_enumerated_sets.py totally_ordered_finite_set.py primes.py \
    all.py positive_integers.py set_from_iterator.py cartesian_product.py \
    integer_range.py finite_enumerated_set.py

sets_LTLIBRARIES = disjoint_set.la finite_set_map_cy.la 

finite_set_map_cy_la_LIBADD = -lcsage

disjoint_set_la_LIBADD = -lgmp -lflint -lcsage
disjoint_set_la_CFLAGS = -std=c99 $(AM_CFLAGS)

.pyx.c:
	$(cython_call)
