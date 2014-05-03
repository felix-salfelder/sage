# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    all.py arxiv_0812_2725.py benchmark.py book_schilling_zabrocki_kschur_primer.py \
    book_stein_ent.py book_stein_modform.py cmdline.py \
    deprecation_test.py \
    __init__.py parigp.py \
    startup.py gap_packages.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = cython.la interrupt.la stl_vector.la

interrupt_la_SOURCES = interrupt.pyx c_lib.c
interrupt_la_LIBADD = @CSAGE_LIBS@

stl_vector_la_LIBADD = @CSAGE_LIBS@ @GMP_OR_MPIR_LIBS@
stl_vector_la_SOURCES = stl_vector.pyxx

tests_french_bookdir = $(instdir)/french_book
tests_french_book_PYTHON = \
    french_book/calculus_doctest.py \
    french_book/domaines_doctest.py \
    french_book/float_doctest.py \
    french_book/__init__.py \
    french_book/integration_doctest.py \
    french_book/linalg_doctest.py \
    french_book/linsolve_doctest.py \
    french_book/mpoly.py \
    french_book/nonlinear_doctest.py \
    french_book/numbertheory.py \
    french_book/polynomes.py \
    french_book/programmation_doctest.py \
    french_book/recequadiff.py
