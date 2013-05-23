# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
gsldir = $(pythondir)/sage/gsl
gsl_PYTHON = __init__.py dft.py all.py

gsl_LTLIBRARIES = callback.la dwt.la fft.la gsl_array.la integration.la interpolation.la ode.la probability_distribution.la 
callback_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@
callback_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
dwt_la_LIBADD = -lgsl -l@BLAS@
dwt_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
fft_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
fft_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
gsl_array_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
gsl_array_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
integration_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
integration_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
interpolation_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
interpolation_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
ode_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
ode_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)
probability_distribution_la_LIBADD = -lgsl -l@BLAS@ -l@BLAS2@ -lcsage
probability_distribution_la_CPPFLAGS = -DGSL_DISABLE_DEPRECATED=1 $(AM_CPPFLAGS)

.pyx.c:
	$(cython_call)
