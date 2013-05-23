# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = integration
include $(top_srcdir)/common.mk
symbolicdir = $(pythondir)/sage/symbolic
symbolic_PYTHON = \
    benchmark.py __init__.py expression_conversions.py operators.py constants.py \
    callable.py units.py relation.py all.py function_factory.py maxima_wrapper.py \
    random_tests.py assumptions.py

symbolic_LTLIBRARIES = constants_c.la expression.la function.la getitem.la pynac.la ring.la 

constants_c_la_LIBADD = -lpynac -lgmp -lcsage
constants_c.cc: @srcdir@/constants_c.pyx
expression_la_LIBADD = -lpynac -lgmp -lcsage
expression.cc: @srcdir@/expression.pyx
function_la_LIBADD = -lpynac -lgmp
function.cc: @srcdir@/function.pyx
getitem_la_LIBADD = -lpynac -lgmp
getitem.cc: @srcdir@/getitem.pyx
pynac_la_LIBADD = -lpynac -lgmp -lgsl -lcsage
pynac.cc: @srcdir@/pynac.pyx
ring_la_LIBADD = -lpynac -lgmp -lcsage
ring.cc: @srcdir@/ring.pyx

.pyx.cc:
	$(cython_call)
