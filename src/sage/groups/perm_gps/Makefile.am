# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = partn_ref partn_ref2
include $(top_srcdir)/common.mk
inst_PYTHON = \
    cubegroup.py __init__.py permgroup_morphism.py permgroup_named.py permgroup.py \
    all.py permutation_groups_catalog.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = permgroup_element.la

permgroup_element_la_LIBADD = @CSAGE_LIBS@
