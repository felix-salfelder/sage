# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = __init__.py all.py

LIBS = @CSAGE_LIBS@

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = chmm.la distributions.la hmm.la util.la
chmm_la_CFLAGS = -std=c99 $(AM_CFLAGS)
chmm_la_CPPFLAGS = $(AM_CPPFLAGS) @PYTHON_INCLUDES@
