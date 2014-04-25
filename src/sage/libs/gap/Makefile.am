# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk

inst_PYTHON = all.py gap_functions.py \
    __init__.py test_long.py \
    context_managers.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = element.la libsagegap.la util.la
element_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@ -lgap -lm
element_la_CPPFLAGS = $(AM_CPPFLAGS)

libsagegap_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@ -lgap -lm
libsagegap_la_CPPFLAGS = $(AM_CPPFLAGS)

util_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@ -lgap -lm
util_la_CPPFLAGS = $(AM_CPPFLAGS)

if HAVE_LIBGAP

AM_CPPFLAGS+=-DHAVE_LIBGAP
CLEANFILES+= libgap.la

else

endif
