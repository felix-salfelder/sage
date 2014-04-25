# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    __init__.py all.py constructor.py function_field.py \
    function_field_ideal.py function_field_order.py maps.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = function_field_element.la
function_field_element_la_LIBADD = @CSAGE_LIBS@
