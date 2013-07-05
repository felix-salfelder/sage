# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
algebras_quatalgdir = $(pythondir)/sage/algebras/quatalg
algebras_quatalg_PYTHON = __init__.py all.py quaternion_algebra.py

algebras_quatalg_LTLIBRARIES = quaternion_algebra_cython.la quaternion_algebra_element.la

quaternion_algebra_cython_la_LIBADD = -lcsage -lflint -lgmp -lgmpxx -lm -lstdc++ -lntl
#quaternion_algebra_cython_la_CPPFLAGS = @LIBFLINT_INCLUDES@
quaternion_algebra_cython.cc: @srcdir@/quaternion_algebra_cython.pyx

quaternion_algebra_element_la_LIBADD = -lcsage -lflint -lgmp -lgmpxx -lm -lstdc++ -lntl
quaternion_algebra_element.cc: @srcdir@/quaternion_algebra_element.pyx

.pyx.cc:
	$(cython_call)
