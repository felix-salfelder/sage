# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
graphs_graph_decompositionsdir = $(pythondir)/sage/graphs/graph_decompositions
graphs_graph_decompositions_PYTHON = __init__.py
graphs_graph_decompositions_LTLIBRARIES = graph_products.la rankwidth.la vertex_separation.la 
rankwidth_la_SOURCES = rankwidth.pyx rankwidth_c/rw.c
rankwidth_la_LIBADD = -lcsage
vertex_separation_la_LIBADD = -lcsage

.pyx.c:
	$(cython_call)
