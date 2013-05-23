# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
libs_gapdir = $(pythondir)/sage/libs/gap
libs_gap_PYTHON = all.py gap_functions.py \
    __init__.py test_long.py \
    context_managers.py

libs_gap_LTLIBRARIES = element.la libsagegap.la util.la
element_la_LIBADD = -lcsage -lgmp -lgap -lm
element_la_CPPFLAGS = -I@SAGE_INC@ $(AM_CPPFLAGS)
libsagegap_la_LIBADD = -lcsage -lgmp -lgap -lm
libsagegap_la_CPPFLAGS = -I@SAGE_INC@ $(AM_CPPFLAGS)
util_la_LIBADD = -lcsage -lgmp -lgap -lm
util_la_CPPFLAGS = -I@SAGE_INC@ $(AM_CPPFLAGS)

.pyx.c:
	$(cython_call)
