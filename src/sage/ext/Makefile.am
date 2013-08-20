# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = interpreters
include $(top_srcdir)/common.mk
extdir = $(pythondir)/sage/ext
ext_PYTHON = gen_interpreters.py __init__.py

AM_DEFAULT_SOURCE_EXT = .pyx
ext_LTLIBRARIES = c_lib.la fast_callable.la fast_eval.la interactive_constructors_c.la multi_modular.la pselect.la
c_lib_la_LIBADD = -lcsage

multi_modular_la_LIBADD = -lgmp -lcsage
multi_modular_la_CFLAGS = $(AM_CFLAGS) -std=c99

fast_callable_la_LIBADD = -lcsage
fast_eval_la_LIBADD = -lcsage

#FIXME (how?)
interpreters-stamp:
	$(PYTHON) @srcdir@/gen_interpreters.py
# this is needed to make cython find the just generated .pxd files
	@VPATH_TRUE@touch interpreters/__init__.py

# FIXME: move to post_commands?
@VPATH_TRUE@all: | __init__.py
@VPATH_TRUE@__init__.py:
@VPATH_TRUE@	touch $@

CLEANFILES+=interpreters-stamp interpreters/wrapper*.p*

noinst_HEADERS = \
    cdefs.pxi gmp.pxi interrupt.pxi python_debug.pxi python.pxi \
    python_rich_object.pxi python_slice.pxi random.pxi signals.pxi \
    stdsage.pxi

all-local: __init__.pyc

.PHONY: interpreters-stamp
