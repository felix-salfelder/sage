# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = backends
include $(top_srcdir)/common.mk
inst_PYTHON = \
    __init__.py \
    all.py \
    interactive_simplex_method.py \
    knapsack.py \
    optimize.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = linear_functions.la mip.la
linear_functions_la_LIBADD = @CSAGE_LIBS@ -lstdc++
linear_functions_la_CPPFLAGS = -I@SAGE_INC@ $(AM_CPPFLAGS)
mip_la_LIBADD = @CSAGE_LIBS@ -lstdc++
mip_la_CPPFLAGS = -I@SAGE_INC@ $(AM_CPPFLAGS)
