# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
# FIXME: are the .xx: srcdir/pyxx rules necessary?
SUBDIRS = padics
include $(top_srcdir)/common.mk
rings_polynomialdir = $(pythondir)/sage/rings/polynomial
rings_polynomial_PYTHON = \
    all.py complex_roots.py convolution.py groebner_fan.py ideal.py \
    infinite_polynomial_element.py infinite_polynomial_ring.py __init__.py \
    laurent_polynomial_ring.py multi_polynomial_element.py \
    multi_polynomial_ideal.py multi_polynomial_ring.py multi_polynomial_sequence.py \
    polynomial_element_generic.py polynomial_fateman.py \
    polynomial_quotient_ring_element.py polynomial_quotient_ring.py \
    polynomial_ring_constructor.py polynomial_ring.py \
    polynomial_singular_interface.py symmetric_ideal.py term_order.py \
    toy_buchberger.py toy_d_basis.py toy_variety.py

rings_polynomial_LTLIBRARIES = \
    cyclotomic.la laurent_polynomial.la multi_polynomial.la \
    multi_polynomial_ideal_libsingular.la multi_polynomial_libsingular.la \
    multi_polynomial_ring_generic.la pbori.la plural.la polydict.la \
    polynomial_compiled.la polynomial_element.la polynomial_gf2x.la \
    polynomial_integer_dense_flint.la polynomial_integer_dense_ntl.la \
    polynomial_modn_dense_ntl.la polynomial_rational_flint.la \
    polynomial_real_mpfr_dense.la polynomial_zmod_flint.la polynomial_zz_pex.la \
    real_roots.la symmetric_reduction.la

laurent_polynomial_la_LIBADD = -lcsage
cyclotomic_la_LIBADD = -lcsage
polydict_la_LIBADD = -lcsage

m4ri_flags_filtered = $(filter-out -std=c99,@M4RI_CFLAGS@)

multi_polynomial_ideal_libsingular_la_LIBADD = -lm -lreadline -lsingular -lgivaro -lntl -lgmpxx -lgmp -lcsage
multi_polynomial_ideal_libsingular_la_SOURCES = multi_polynomial_ideal_libsingular.pyxx
multi_polynomial_ideal_libsingular.cc: @srcdir@/multi_polynomial_ideal_libsingular.pyxx
multi_polynomial_ideal_libsingular_la_CXXFLAGS = -D__STDC_LIMIT_MACROS $(AM_CXXFLAGS)
multi_polynomial_ideal_libsingular_la_CPPFLAGS = $(AM_CPPFLAGS) \
                                                 @SINGULAR_INCLUDES@

multi_polynomial_la_LIBADD = -lcsage

multi_polynomial_ring_generic_la_LIBADD = -lcsage

multi_polynomial_libsingular_la_LIBADD = -lm -lreadline -lsingular -lgivaro -lntl -lgmpxx -lgmp -lcsage
multi_polynomial_libsingular_la_SOURCES = multi_polynomial_libsingular.pyxx
multi_polynomial_libsingular.cc: @srcdir@/multi_polynomial_libsingular.pyxx
multi_polynomial_libsingular_la_CPPFLAGS = $(AM_CPPFLAGS) -D__STDC_LIMIT_MACROS \
                                           @SINGULAR_INCLUDES@

pbori_la_LIBADD = -lpolybori-0.8 -lpolybori_groebner-0.8 -lm4ri -lpng12 -lcsage
pbori_la_SOURCES = pbori.pyxx
pbori.cc: @srcdir@/pbori.pyxx
pbori_la_CXXFLAGS = $(m4ri_flags_filtered) $(AM_CXXFLAGS)
pbori_la_CPPFLAGS = $(AM_CPPFLAGS) -I@SAGE_DIR@/libs/polybori

plural_la_LIBADD = -lm -lreadline -lsingular -lgivaro -lgmpxx -lgmp -lcsage
plural_la_SOURCES = plural.pyxx
plural.cc: @srcdir@/plural.pyxx
plural_la_CPPFLAGS = $(AM_CPPFLAGS) -D__STDC_LIMIT_MACROS \
                     @SINGULAR_INCLUDES@

polynomial_element_la_LIBADD = -lcsage

polynomial_gf2x_la_LIBADD = -lntl -lstdc++ -lgmp
polynomial_gf2x_la_SOURCES = polynomial_gf2x.pyxx
polynomial_gf2x.cc: @srcdir@/polynomial_gf2x.pyxx
polynomial_gf2x_la_CXXFLAGS = $(AM_CXXFLAGS) $(m4ri_flags_filtered)
polynomial_gf2x_la_CPPFLAGS = -I@SAGE_DIR@/libs/ntl/ $(AM_CPPFLAGS)

polynomial_integer_dense_flint_la_LIBADD = -lcsage -lflint -lntl -lgmpxx -lgmp
polynomial_integer_dense_flint_la_SOURCES = polynomial_integer_dense_flint.pyxx
polynomial_integer_dense_flint.cc: @srcdir@/polynomial_integer_dense_flint.pyxx

polynomial_integer_dense_ntl_la_LIBADD = -lntl -lstdc++ -lgmp
polynomial_integer_dense_ntl.cc: @srcdir@/polynomial_integer_dense_ntl.pyxx
polynomial_integer_dense_ntl_la_SOURCES = polynomial_integer_dense_ntl.pyxx

polynomial_integer_dense_ntl_la_CPPFLAGS = -I@SAGE_DIR@/libs/ntl $(AM_CPPFLAGS)

polynomial_modn_dense_ntl_la_LIBADD = -lntl -lstdc++ -lgmp -lcsage
polynomial_modn_dense_ntl_la_SOURCES = polynomial_modn_dense_ntl.pyxx
polynomial_modn_dense_ntl.cc: @srcdir@/polynomial_modn_dense_ntl.pyxx
polynomial_modn_dense_ntl_la_CPPFLAGS = -I@SAGE_DIR@/libs/ntl $(AM_CPPFLAGS)

polynomial_rational_flint_la_LIBADD = -lcsage -lflint -lntl -lgmpxx -lgmp
polynomial_rational_flint_la_SOURCES = polynomial_rational_flint.pyxx
polynomial_rational_flint.cc: @srcdir@/polynomial_rational_flint.pyxx

polynomial_real_mpfr_dense_la_LIBADD = -lmpfr -lgmp -lcsage

polynomial_zmod_flint_la_LIBADD = -lcsage -lflint -lgmp -lgmpxx -lntl -lzn_poly
polynomial_zmod_flint_la_SOURCES = polynomial_zmod_flint.pyxx
polynomial_zmod_flint.cc: @srcdir@/polynomial_zmod_flint.pyxx

polynomial_zz_pex_la_LIBADD = -lntl -lstdc++ -lgmp
polynomial_zz_pex_la_SOURCES = polynomial_zz_pex.pyxx
polynomial_zz_pex.cc: @srcdir@/polynomial_zz_pex.pyxx
polynomial_zz_pex_la_CPPFLAGS = -I@SAGE_DIR@/libs/ntl $(AM_CPPFLAGS)

real_roots_la_LIBADD = -lmpfr -lgmp
real_roots_la_CPPFLAGS = -I@numpy_include_dir@ $(AM_CPPFLAGS)

.pyx.c:
	$(cython_call)
.pyx.cc:
	$(CYTHONCPP) $(CYTHONFLAGS) $< -o $@ -MF $(DEPDIR)/$*.PcythonT
	$(cython_call)

%.pyxx: @srcdir@/%.pyx
	ln -s $< $@

# FIXME. something extremely wrong with singular
multi_polynomial_ideal_libsingular_la_CPPFLAGS += -DNDEBUG
multi_polynomial_libsingular_la_CPPFLAGS += -DNDEBUG
plural_la_CPPFLAGS += -DNDEBUG
