# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    __init__.py all.py chow_group.py divisor.py fano_variety.py homset.py \
    ideal.py library.py morphism.py \
    points.py \
    variety.py \
    weierstrass.py \
    weierstrass_covering.py \
    weierstrass_higher.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = divisor_class.la
divisor_class_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@
