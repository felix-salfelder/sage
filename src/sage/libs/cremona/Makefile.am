# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
libs_cremonadir = $(pythondir)/sage/libs/cremona
libs_cremona_PYTHON = __init__.py constructor.py all.py
libs_cremona_LTLIBRARIES = homspace.la mat.la newforms.la

homspace_la_LIBADD = -lec -lntl -lpari -lgmpxx -lgmp -lm -lcsage
homspace.cc: @srcdir@/homspace.pyx
homspace_la_CPPFLAGS = -DNTL_ALL $(AM_CPPFLAGS)
mat_la_LIBADD = -lec -lntl -lpari -lgmpxx -lgmp -lm
mat.cc: @srcdir@/mat.pyx
mat_la_CPPFLAGS = -DNTL_ALL $(AM_CPPFLAGS)
newforms_la_LIBADD = -lec -lntl -lpari -lgmpxx -lgmp -lm -lcsage
newforms.cc: @srcdir@/newforms.pyx
newforms_la_CPPFLAGS = -DNTL_ALL $(AM_CPPFLAGS)

.pyx.cc:
	$(cython_call)
