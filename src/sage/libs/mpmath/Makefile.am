# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
libs_mpmathdir = $(pythondir)/sage/libs/mpmath
libs_mpmath_PYTHON = __init__.py all.py

libs_mpmath_LTLIBRARIES = ext_impl.la ext_libmp.la ext_main.la utils.la 
ext_impl_la_LIBADD = -lmpfr -lgmp
ext_libmp_la_LIBADD = -lgmp
ext_main_la_LIBADD = -lgmp
utils_la_LIBADD = -lmpfr -lgmp -lcsage

.pyx.c:
	$(cython_call)
