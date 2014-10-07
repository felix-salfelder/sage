# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    __init__.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = \
    autgroup_can_label.la \
    codecan.la

codecan_la_CPPFLAGS = -I$(abs_top_builddir)/libs/gap $(AM_CPPFLAGS)

noinst_HEADERS = codecan.pxd

# _la_LIBADD = @CSAGE_LIBS@
