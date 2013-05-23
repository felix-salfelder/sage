# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
if USE_LIBCRYPTOMINISAT
COND_CMS = cryptominisat
endif

SUBDIRS = $(COND_CMS)
include $(top_srcdir)/common.mk
sat_solversdir = $(pythondir)/sage/sat/solvers
sat_solvers_PYTHON = __init__.py dimacs.py
sat_solvers_LTLIBRARIES = satsolver.la

.pyx.c:
	$(cython_call)
