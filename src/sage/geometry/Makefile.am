# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = triangulation
include $(top_srcdir)/common.mk
inst_PYTHON = \
    cone.py polyhedra.py __init__.py fan_isomorphism.py toric_plotter.py \
    fan_morphism.py fan.py all.py hasse_diagram.py lattice_polytope.py polytope.py \
    toric_lattice.py newton_polygon.py pseudolines.py \
    linear_expression.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = integral_points.la point_collection.la toric_lattice_element.la
toric_lattice_element_la_LIBADD = @GMP_OR_MPIR_LIBS@ @CSAGE_LIBS@

hpdir = $(instdir)/hyperplane_arrangement
hp_PYTHON = \
    hyperplane_arrangement/affine_subspace.py \
    hyperplane_arrangement/arrangement.py \
    hyperplane_arrangement/hyperplane.py \
    hyperplane_arrangement/__init__.py \
    hyperplane_arrangement/library.py \
    hyperplane_arrangement/plot.py

geometry_polyhedrondir = $(instdir)/polyhedron
geometry_polyhedron_PYTHON = \
    polyhedron/all.py \
    polyhedron/backend_cdd.py \
    polyhedron/backend_ppl.py \
    polyhedron/base.py \
    polyhedron/base_QQ.py \
    polyhedron/base_RDF.py \
    polyhedron/base_ZZ.py \
    polyhedron/cdd_file_format.py \
    polyhedron/constructor.py \
    polyhedron/face.py \
    polyhedron/__init__.py \
    polyhedron/library.py \
    polyhedron/misc.py \
    polyhedron/palp_database.py \
    polyhedron/parent.py \
    polyhedron/plot.py \
    polyhedron/ppl_lattice_polytope.py \
    polyhedron/representation.py \
    polyhedron/lattice_euclidean_group_element.py \
    polyhedron/ppl_lattice_polygon.py

geom_riemanndir = $(instdir)/riemannian_manifolds
geom_riemann_PYTHON = \
    riemannian_manifolds/all.py \
    riemannian_manifolds/__init__.py \
    riemannian_manifolds/parametrized_surface3d.py \
    riemannian_manifolds/surface3d_generators.py
