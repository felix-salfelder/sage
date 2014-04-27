# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = __init__.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = \
    refinement_generic.la

# all of them (correct?)
LIBS += @CSAGE_LIBS@
AM_CPPFLAGS += -I@top_builddir@/libs/gap

refinement_generic_la_LIBADD = @GMP_OR_MPIR_LIBS@ -lflint

noinst_HEADERS = \
    refinement_generic.pxd
