# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
if USE_LIBCOXETER3
COND_COXETER3 = coxeter3
endif
if USE_LIBLRCALC
COND_LRCALC = lrcalc
endif

SUBDIRS = \
    $(COND_COXETER3) cremona flint fplll gap lcalc \
    linbox $(COND_LRCALC) mpmath mwrank ntl pari singular symmetrica

include $(top_srcdir)/common.mk
libsdir = $(pythondir)/sage/libs
libs_PYTHON = __init__.py all.py
libs_LTLIBRARIES = ecl.la libsageecm.la ppl.la ratpoints.la
ecl_la_LIBADD = -lecl -lgmp -lcsage
ecl_la_CPPFLAGS = -I@SAGE_INC@/ecl $(AM_CPPFLAGS)
libsageecm_la_LIBADD = -lecm -lgmp
ppl_la_SOURCES = ppl.pyxx ppl_shim.cc
ppl_la_LIBADD = -lppl -lgmpxx -lgmp -lm -lcsage
ppl.cc: @srcdir@/ppl.pyxx
ratpoints_la_LIBADD = -lratpoints -lgmp

libs_gmpdir = $(libsdir)/gmp
libs_gmp_PYTHON = __init__.py

.pyx.c:
	$(cython_call)
