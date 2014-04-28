# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = __init__.py all.py gen_py.py

LIBS = @CSAGE_LIBS@
AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = \
    gen.la \
    handle_error.la \
    pari_instance.la

gen_la_LIBADD = -lpari @GMP_OR_MPIR_LIBS@

noinst_HEADERS = handle_error.pxd pari_instance.pxd
