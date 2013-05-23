# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
libs_fpllldir = $(pythondir)/sage/libs/fplll
libs_fplll_PYTHON = __init__.py

libs_fplll_LTLIBRARIES = fplll.la

fplll_la_LIBADD = -lgmp -lmpfr -lfplll -lcsage
fplll.cc: @srcdir@/fplll.pyx
fplll_la_CPPFLAGS = @FPLLL_INCLUDES@ -DFPLLL_V3_COMPAT $(AM_CPPFLAGS)
.pyx.cc:
	$(cython_call)
