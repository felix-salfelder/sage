# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = abelian_gps perm_gps matrix_gps semimonomial_transformations
include $(top_srcdir)/common.mk
inst_PYTHON = \
    braid.py __init__.py class_function.py generic.py pari_group.py \
    free_group.py all.py group_homset.py groups_catalog.py conjugacy_classes.py \
    finitely_presented.py \
    libgap_group.py libgap_mixin.py \
    finitely_presented_catalog.py \
    finitely_presented_named.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = group.la libgap_wrapper.la old.la

groups_additive_abeliandir = $(instdir)/additive_abelian
groups_additive_abelian_PYTHON = \
    additive_abelian/additive_abelian_group.py \
    additive_abelian/additive_abelian_wrapper.py \
    additive_abelian/all.py \
    additive_abelian/__init__.py

groups_misc_gpsdir = $(instdir)/misc_gps
groups_misc_gps_PYTHON = \
    misc_gps/__init__.py \
    misc_gps/misc_groups_catalog.py \
    misc_gps/misc_groups.py

groups_affine_gpsdir = $(instdir)/affine_gps
groups_affine_gps_PYTHON = \
    affine_gps/affine_group.py \
    affine_gps/euclidean_group.py \
    affine_gps/group_element.py \
    affine_gps/__init__.py

# not using config.h ... (for now?)
if HAVE_LIBGAP
LIBGAP_ARG=-DHAVE_LIBGAP
endif

libgap_wrapper_la_CPPFLAGS = -I@top_builddir@/libs/gap $(LIBGAP_ARG) $(AM_CPPFLAGS)
