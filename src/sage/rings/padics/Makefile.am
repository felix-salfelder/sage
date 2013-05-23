# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
rings_padicsdir = $(pythondir)/sage/rings/padics
rings_padics_PYTHON = \
    all.py eisenstein_extension_generic.py factory.py generic_nodes.py __init__.py \
    local_generic.py misc.py padic_base_generic.py padic_base_leaves.py \
    padic_extension_generic.py padic_extension_leaves.py padic_generic.py \
    precision_error.py tests.py tutorial.py unramified_extension_generic.py

rings_padics_LTLIBRARIES = \
    local_generic_element.la padic_ZZ_pX_CA_element.la \
    padic_ZZ_pX_CR_element.la padic_ZZ_pX_FM_element.la padic_ZZ_pX_element.la \
    padic_base_coercion.la padic_base_generic_element.la \
    padic_capped_absolute_element.la padic_capped_relative_element.la \
    padic_ext_element.la padic_fixed_mod_element.la padic_generic_element.la \
    padic_printing.la pow_computer.la pow_computer_ext.la

padic_ZZ_pX_CA_element_la_LIBADD = -lntl -lgmp -lcsage -lgmpxx -lm -lstdc++
padic_ZZ_pX_CA_element.cc: @srcdir@/padic_ZZ_pX_CA_element.pyxx
padic_ZZ_pX_CA_element_la_SOURCES = padic_ZZ_pX_CA_element.pyxx

padic_ZZ_pX_CR_element_la_LIBADD = -lntl -lgmp -lcsage -lgmpxx -lm -lstdc++
padic_ZZ_pX_CR_element.cc: @srcdir@/padic_ZZ_pX_CR_element.pyx
padic_ZZ_pX_FM_element_la_LIBADD = -lntl -lgmp -lcsage -lgmpxx -lm -lstdc++
padic_ZZ_pX_FM_element.cc: @srcdir@/padic_ZZ_pX_FM_element.pyx
padic_ZZ_pX_element_la_LIBADD = -lntl -lgmp -lcsage -lgmpxx -lm -lstdc++
padic_ZZ_pX_element.cc: @srcdir@/padic_ZZ_pX_element.pyx
padic_base_coercion_la_LIBADD = -lgmp -lcsage
padic_base_generic_element_la_LIBADD = -lgmp
padic_capped_absolute_element_la_LIBADD = -lgmp -lcsage
padic_capped_relative_element_la_LIBADD = -lgmp -lcsage
padic_ext_element_la_LIBADD = -lntl -lgmp -lcsage -lgmpxx -lm -lstdc++
padic_ext_element.cc: @srcdir@/padic_ext_element.pyx
padic_fixed_mod_element_la_LIBADD = -lgmp -lcsage
padic_generic_element_la_LIBADD = -lgmp -lcsage

padic_printing_la_LIBADD = -lgmp -lntl -lcsage -lgmpxx -lm -lstdc++
padic_printing.cc: @srcdir@/padic_printing.pyx
pow_computer_la_LIBADD = -lcsage -lntl -lgmp -lgmpxx -lm -lstdc++
pow_computer.cc: @srcdir@/pow_computer.pyx
pow_computer_ext_la_LIBADD = -lcsage -lntl -lgmp -lgmpxx -lm -lstdc++
pow_computer_ext.cc: @srcdir@/pow_computer_ext.pyx

.pyx.c:
	$(cython_call)
.pyx.cc:
	$(cython_call)
