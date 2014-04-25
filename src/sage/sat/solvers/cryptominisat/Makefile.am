# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = __init__.py

AM_DEFAULT_SOURCE_EXT = .pyxx
inst_LTLIBRARIES = cryptominisat.la solverconf.la
cryptominisat_la_LIBADD = -lcryptominisat -lz
cryptominisat_la_CPPFLAGS = -I@SAGE_LOCAL@/include -I@SAGE_LOCAL@/include/cmsat $(AM_CPPFLAGS)

solverconf_la_SOURCES = solverconf.pyxx solverconf_helper.cpp
solverconf_la_LIBADD = -lcryptominisat -lz
solverconf_la_CPPFLAGS = -I@SAGE_LOCAL@/include -I@SAGE_LOCAL@/include/cmsat $(AM_CPPFLAGS)
