# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = integration
include $(top_srcdir)/common.mk
inst_PYTHON = \
    benchmark.py \
    complexity_measures.py \
    __init__.py expression_conversions.py operators.py constants.py \
    callable.py units.py relation.py all.py function_factory.py maxima_wrapper.py \
    random_tests.py assumptions.py \
    tests.py

inst_LTLIBRARIES = \
    constants_c.la \
    expression.la \
	 function.la \
	 getitem.la \
    pynac.la \
    ring.la \
    substitution_map.la

# all?
LIBS = -lpynac

AM_DEFAULT_SOURCE_EXT = .pyxx
constants_c_la_LIBADD = @GMP_OR_MPIR_LIBS@ @CSAGE_LIBS@
expression_la_LIBADD = @GMP_OR_MPIR_LIBS@ @CSAGE_LIBS@
function_la_LIBADD = @GMP_OR_MPIR_LIBS@
getitem_la_LIBADD = @GMP_OR_MPIR_LIBS@
pynac_la_LIBADD = @GMP_OR_MPIR_LIBS@ -lgsl @CSAGE_LIBS@
ring_la_LIBADD = @GMP_OR_MPIR_LIBS@ @CSAGE_LIBS@
substitution_map_la_LIBADD = @CSAGE_LIBS@

noinst_HEADERS = ginac.pxd ginac_wrap.h substitution_map.pxd
