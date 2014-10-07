# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    all.py \
    bessel.py \
    exp_integral.py \
    generalized.py \
    hyperbolic.py \
    hypergeometric.py \
    __init__.py \
    jacobi.py \
    log.py \
    min_max.py \
    orthogonal_polys.py \
    other.py \
    piecewise.py \
    special.py \
    spike_function.py \
    transcendental.py \
    trig.py \
    wigner.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = prime_pi.la
prime_pi_la_LIBADD = @CSAGE_LIBS@
