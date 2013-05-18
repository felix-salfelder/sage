
AC_CONFIG_SRCDIR([graphs/graph_bundle.py])
AC_CONFIG_MACRO_DIR([m4])
AC_INIT([python-sage], [none], [sage-support@googlegroups.com])
AC_CONFIG_AUX_DIR([.])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])

AM_PROG_AR
LT_INIT

AC_PROG_CC
AC_PROG_CXX

# AC_SUBST(AM_DEFAULT_SOURCE_EXT,.pyx)

## environment
AC_ARG_VAR(CPPFLAGS, cppflags)
AC_ARG_VAR(LDFLAGS, ldflags)
AC_ARG_VAR(PATH, path)

## defaults
AC_SUBST(AM_LDFLAGS, "-module -avoid-version")

## python stuff
AM_PATH_PYTHON([2.7])

AC_PATH_PROGS([CYTHON],
              [cython2.7 cython],
              [no])
AS_IF([test "$CYTHON" = no], [AC_MSG_ERROR([cannot find cython.])])

AM_PATH_PYTHON([2.7])
AM_CHECK_PYTHON_HEADERS()
PYTHON_INCLUDE_DIR=$PYTHON_PREFIX/include
PYTHON_LIB_DIR=$PYTHON_PREFIX/lib

AC_ARG_WITH(python-include-dir,
            [  --with-python-include-dir=DIR look in DIR for Python headers],
            [PYTHON_INCLUDE_DIR=$withval],)
AC_SUBST(PYTHON_INCLUDE_DIR)
CPPFLAGS="$CPPFLAGS $PYTHON_INCLUDES"
AC_ARG_WITH(python-lib-dir,
            [  --with-python-lib-dir=DIR look in DIR for Python libraries],
            [PYTHON_LIB_DIR=$withval],)
AC_SUBST(PYTHON_LIB_DIR)

# find clib. might be obsolete
# AC_ARG_WITH(blas, --with-clib   choose c_lib, [clib=$with_clib], [])

# not fetching from environment. use --with-blas
blas=
blas2=

## Choose cblas library -- note -- make sure to update sage/misc/cython.py
## if you change this!!
AC_ARG_WITH(blas,   --with-blas   choose cblas, [blas=$with_blas], [])

if test -n "${blas}"; then
  AC_CHECK_LIB([$blas], [cblas_dgemv], [blas2=$blas],
					[ AC_MSG_ERROR(user specified blas doesnt exist) ]
              )
fi

if test -z "${blas}"; then
  # we cannot know whether this is sage-distributed atlas.
  # and it doesnt matter.
  AC_CHECK_LIB([atlas], [ATL_scpsc], [blas=cblas; blas2=atlas], [])
  # some random symbol   ^
fi

if test -z "${blas}"; then
  AC_CHECK_LIB([cblas], [cblas_dgemv], [blas=cblas; blas2=atlas], [])
fi

if test -z "${blas}"; then
  AC_CHECK_LIB([blas], [cblas_dgemv], [blas=gslcblas; blas2=gslcblas], [])
fi

if test -z "${blas}"; then
  AC_CHECK_LIB([gslcblas], [cblas_dgemv], [blas=gslcblas; blas2=gslcblas], [])
fi

if test -z "${blas}"; then
	AC_MSG_ERROR([couldn't find any blas])
fi

#if -z os.environ.has_key('SAGE_BLAS'):
#    BLAS=os.environ['SAGE_BLAS']
#    BLAS2=os.environ['SAGE_BLAS']
#	 AC_MSG_RESULT(from environment: ${BLAS})
#elif os.path.exists('%s/lib/libatlas.so'%os.environ['SAGE_LOCAL']):
#    BLAS='cblas'
#    BLAS2='atlas'
#elif os.path.exists('/usr/lib/libcblas.dylib') or \
#     os.path.exists('/usr/lib/libcblas.so'):
#    BLAS='cblas'
#    BLAS2='atlas'
#elif os.path.exists('/usr/lib/libblas.dll.a'):
#    BLAS='gslcblas'
#    BLAS2='gslcblas'
#else:
#    # This is very slow  (?), but *guaranteed* to be available.
#    BLAS='gslcblas'
#    BLAS2='gslcblas'
#	 AC_MSG_RESULT(fallback to gslcblas)

#########################################################
### M4RI flags
#########################################################

# TODO!
# import ast
# m4ri_extra_compile_args = ["-std=c99"]
# for line in open(SAGE_INC + "/m4ri/m4ri_config.h"):
#     if not line.startswith("#define __M4RI_SIMD_CFLAGS"):
#         continue
#     m4ri_sse2_cflags = ast.literal_eval(line[len("#define __M4RI_SIMD_CFLAGS"):].strip())
#     m4ri_extra_compile_args.extend( [flag.strip() for flag in m4ri_sse2_cflags.split(" ") if flag.strip()] )
#     break

AC_SUBST(BLAS, ${blas})
AC_SUBST(BLAS2, ${blas2})

sage_local=$prefix
test "x$prefix" = xNONE &&  sage_local=$ac_default_prefix
AC_SUBST(SAGE_LOCAL, $sage_local)

# ouch
# CPPFLAGS='-I$(top_srcdir)/../c_lib/include'

AC_CONFIG_FILES([
    setup.py
    module_list.py
    Makefile
    calculus/Makefile
    categories/Makefile
    coding/Makefile
    combinat/Makefile
    crypto/Makefile
    ext/Makefile
    finance/Makefile
    functions/Makefile
    games/Makefile
    geometry/Makefile
    graphs/Makefile
    groups/Makefile
    gsl/Makefile
    interacts/Makefile
    libs/Makefile
    matrix/Makefile
    media/Makefile
    misc/Makefile
    modules/Makefile
    numerical/Makefile
    plot/Makefile
    quadratic_forms/Makefile
    rings/Makefile
    sets/Makefile
    stats/Makefile
    structure/Makefile
    symbolic/Makefile
    tests/Makefile
    algebras/letterplace/Makefile
    algebras/quatalg/Makefile
    categories/examples/Makefile
    combinat/matrices/Makefile
    combinat/words/Makefile
    geometry/triangulation/Makefile
    graphs/base/Makefile
    graphs/graph_decompositions/Makefile
    graphs/modular_decomposition/Makefile
    groups/perm_gps/Makefile
    libs/cremona/Makefile
    libs/flint/Makefile
    libs/fplll/Makefile
    libs/gap/Makefile
    libs/lcalc/Makefile
    libs/linbox/Makefile
    libs/mpmath/Makefile
    libs/mwrank/Makefile
    libs/ntl/Makefile
    libs/pari/Makefile
    libs/singular/Makefile
    libs/symmetrica/Makefile
    modular/arithgroup/Makefile
    modular/modform/Makefile
    modular/modsym/Makefile
    numerical/backends/Makefile
    plot/plot3d/Makefile
    rings/finite_rings/Makefile
    rings/function_field/Makefile
    rings/number_field/Makefile
    rings/padics/Makefile
    rings/polynomial/Makefile
    rings/universal_cyclotomic_field/Makefile
    sat/solvers/Makefile
    schemes/elliptic_curves/Makefile
    schemes/hyperelliptic_curves/Makefile
    schemes/toric/Makefile
    stats/hmm/Makefile
    groups/perm_gps/partn_ref/Makefile
])

AC_OUTPUT

AC_MSG_RESULT([
** Configuration summary for $PACKAGE $VERSION:

   prefix:     $prefix
   exec_prefix:$exec_prefix
   libdir:     $libdir
   CPPFLAGS:   $CPPFLAGS
   CFLAGS:     $CFLAGS
   CXXFLAGS:   $CXXFLAGS
   LDFLAGS:    $LDFLAGS
   LIBS:       $LIBS
   c_lib:      $clib
   BLAS:       $blas
   BLAS2:      $blas2

   builddir:   $ac_abs_builddir
   srcdir:     $ac_abs_srcdir
])

# vim:et
