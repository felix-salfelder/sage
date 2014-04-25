# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = __init__.py all.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = ext_impl.la ext_libmp.la ext_main.la utils.la
ext_impl_la_LIBADD = @CSAGE_LIBS@ -lmpfr @GMP_OR_MPIR_LIBS@
ext_libmp_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@
ext_main_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@
utils_la_LIBADD = -lmpfr @GMP_OR_MPIR_LIBS@ @CSAGE_LIBS@
