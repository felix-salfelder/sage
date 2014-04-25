# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    __init__.py algebra.py all.py calculus.py debugger.py fractals.py geometry.py \
    library.py statistics.py
AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = library_cython.la
library_cython_la_LIBADD = @CSAGE_LIBS@
