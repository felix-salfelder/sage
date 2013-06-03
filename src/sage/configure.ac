
AC_CONFIG_SRCDIR([graphs/graph_bundle.py])
AC_CONFIG_MACRO_DIR([m4])
AC_INIT([python-sage], [none], [sage-support@googlegroups.com])
AM_SILENT_RULES
AC_CONFIG_AUX_DIR([.])
AC_CONFIG_HEADER([config.h])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])

# this is not in stable automake yet
# AM_EXTRA_RECURSIVE_TARGETS([py])

AM_PROG_AR
LT_INIT([disable-static])

AC_PROG_CC
AC_PROG_CXX
AC_PROG_LN_S

# AC_SUBST(AM_DEFAULT_SOURCE_EXT,.pyx)

## environment,
# see autoconf/manual/autoconf-2.60/html_node/Setting-Output-Variables.html,
# particularly: "variable is kept during automatic reconfiguration"
AC_ARG_VAR(CPPFLAGS, cppflags)
AC_ARG_VAR(LDFLAGS, ldflags)
AC_ARG_VAR(PATH, path)
AC_ARG_VAR(PYTHONPATH, pythonpath)

sage_local=$prefix
test "x$prefix" = xNONE &&  sage_local=$ac_default_prefix
AC_SUBST(SAGE_LOCAL, $sage_local)

## VPATH
AM_CONDITIONAL([VPATH_BUILD], [test ! x$srcdir = "x."])

# FIXME: use VPATH_BUILD_{TRUE/FALSE}
VPATH_TRUE=
VPATH_FALSE=#
if test x$srcdir = "x."; then
  VPATH_TRUE=#
  VPATH_FALSE=
fi
AC_SUBST(VPATH_TRUE)
AC_SUBST(VPATH_FALSE)
## defaults
AC_SUBST(AM_LDFLAGS, "-module -avoid-version")

## python stuff
python_version_required=2.7
AM_PATH_PYTHON([$python_version_required])
if ! test x$PYTHON_VERSION = x"$python_version_required"; then
   AC_MSG_ERROR([python $PYTHON_VERSION is not $python_version_required])
fi
AM_PATH_PYTHON([2.7])

AC_PATH_PROGS([CYTHON],
              [cython2.7 cython],
              [no])
AS_IF([test "$CYTHON" = no], [AC_MSG_ERROR([cannot find cython.])])

AM_CHECK_PYTHON_HEADERS()
PYTHON_INCLUDE_DIR=$PYTHON_PREFIX/include
PYTHON_LIB_DIR=$PYTHON_PREFIX/lib

AC_ARG_WITH(python-include-dir,
            [  --with-python-include-dir=DIR look in DIR for Python headers],
            [PYTHON_INCLUDE_DIR=$withval],)
AC_SUBST(PYTHON_INCLUDE_DIR)
my_CPPFLAGS="$CPPFLAGS $PYTHON_INCLUDES"
AC_ARG_WITH(python-lib-dir,
            [  --with-python-lib-dir=DIR look in DIR for Python libraries],
            [PYTHON_LIB_DIR=$withval],)
AC_SUBST(PYTHON_LIB_DIR)

AC_MSG_CHECKING([whether jinja2 is available])
if ! $PYTHON -c import\ jinja2 &>/dev/null; then
   AC_MSG_RESULT([no])
   AC_MSG_ERROR([no jinja2])
fi
AC_MSG_RESULT([yes])

AC_MSG_CHECKING([whether $CYTHON supports dependencies])
if $CYTHON --help | grep -q 'dependency makefile'; then
   pydep=yes
else
   pydep=no
fi
AC_MSG_RESULT($pydep)
AM_CONDITIONAL([PYDEP], [test $pydep = yes])

# find clib. might be obsolete
# AC_ARG_WITH(blas, --with-clib   choose c_lib, [clib=$with_clib], [])

### singular
AC_PATH_PROGS([SINGULAR],
              [Singular singular],
              [no])
AS_IF([test "$SINGULAR" = no], [AC_MSG_ERROR([cannot find singular.])])
# HACK: don't know how to retrieve share from Singular
SINGULAR_SHARE=`dirname $SINGULAR`/../share/singular
if test ! -e $SINGULAR_SHARE/algebra.lib; then
	AC_MSG_NOTICE([unexpected singular install, cannot find share])
fi
AC_SUBST([SINGULAR_SHARE])
SINGULAR_BIN=`dirname $SINGULAR`
AC_SUBST([SINGULAR_BIN])

# singular needs singular and factory
OLDCPPFLAGS=$CPPFLAGS
CPPFLAGS=" -I`dirname $SINGULAR`/../include/singular -I`dirname $SINGULAR`/../include/factory"
AC_CHECK_HEADER([si_gmp.h],,[AC_MSG_ERROR(cannot find singular header)])
SINGULAR_INCLUDES=$CPPFLAGS
AC_SUBST([SINGULAR_INCLUDES])
CPPFLAGS=$OLDCPPFLAGS

print currently $CPPFLAGS

# just check, for now
AC_CHECK_HEADER([cliquer/cliquer.h],,[AC_MSG_ERROR(cannot find cliquer header)])
AC_CHECK_HEADER([flint/fmpz.h],,[AC_MSG_ERROR(cannot find flint header)])
AC_CHECK_HEADER([zn_poly/zn_poly.h],,[AC_MSG_ERROR(cannot find zn_poly header)])


AC_LANG_PUSH([C++])
AC_CHECK_HEADER([fplll.h],,[AC_MSG_ERROR(cannot find fplll header)])
AC_CHECK_HEADER([fplll/fplll.h],,[AC_MSG_ERROR(cannot find fplll header)])
AC_LANG_POP
AC_SUBST([FPLLL_INCLUDES]) dnl currently unneeded
# not yet
# AC_CHECK_HEADER([gap/libgap.h],,[AC_MSG_ERROR(cannot find libgap header)])

# extra packages: FIXME: just allow sage packages, if desired
AC_CHECK_HEADER([coxeter3.h], [HAVE_LIBCOXETER3=1], [HAVE_LIBCOXETER3=0])
AC_SUBST([HAVE_LIBCOXETER3])
AM_CONDITIONAL([USE_LIBCOXETER3], [ test $HAVE_LIBCOXETER3 -eq 1 ])

AC_CHECK_HEADER([fes.h], [HAVE_LIBFES=1], [HAVE_LIBFES=0])
AC_SUBST([HAVE_LIBFES])
AM_CONDITIONAL([USE_LIBFES], [ test $HAVE_LIBFES -eq 1 ])

# this is a hack, better use AC_ARG_WITH (?)
AC_MSG_CHECKING("lrcalc includedir")
AS_IF([test -f $sage_local/include/lrcalc/vector.h],
      [LIBLRCALC_INCLUDES="-I$sage_local/include/lrcalc"
      AC_MSG_RESULT([$sage_local/include/lrcalc/])],
      [AC_MSG_RESULT([nothing special])])
CPPFLAGS_SAVE=$CPPFLAGS
CPPFLAGS+=" $LIBLRCALC_INCLUDES"
AC_CHECK_HEADER([symfcn.h], [HAVE_LIBLRCALC=1], [HAVE_LIBLRCALC=0])
CPPFLAGS=$CPPFLAGS_SAVE
AC_SUBST([HAVE_LIBLRCALC])
AM_CONDITIONAL([USE_LIBLRCALC], [ test $HAVE_LIBLRCALC -eq 1 ])
AC_SUBST([LIBLRCALC_INCLUDES])

AC_CHECK_HEADER([gurobi.h], [HAVE_LIBGUROBI=1], [HAVE_LIBGUROBI=0])
AC_SUBST([HAVE_LIBGUROBI])
AM_CONDITIONAL([USE_LIBGUROBI], [ test $HAVE_LIBGUROBI -eq 1 ])

AC_CHECK_HEADER([cbc.h], [HAVE_LIBCBC=1], [HAVE_LIBCBC=0])
AC_SUBST([HAVE_LIBCBC])
AM_CONDITIONAL([USE_LIBCBC], [ test $HAVE_LIBCBC -eq 1 ])

AC_CHECK_HEADER([cplex.h], [HAVE_LIBCPLEX=1], [HAVE_LIBCPLEX=0])
AC_SUBST([HAVE_LIBCPLEX])
AM_CONDITIONAL([USE_LIBCPLEX], [ test $HAVE_LIBCPLEX -eq 1 ])

AC_CHECK_HEADER([coin.h], [HAVE_LIBCOIN=1], [HAVE_LIBCOIN=0])
AC_SUBST([HAVE_LIBCOIN])
AM_CONDITIONAL([USE_LIBCOIN], [ test $HAVE_LIBCOIN -eq 1 ])

AC_CHECK_HEADER([Solver.h], [HAVE_LIBCRYPTOMINISAT=1], [HAVE_LIBCRYPTOMINISAT=0])
AC_SUBST([HAVE_LIBCRYPTOMINISAT])
AM_CONDITIONAL([USE_LIBCRYPTOMINISAT], [ test $HAVE_LIBCRYPTOMINISAT -eq 1 ])

AC_CHECK_LIB([readline], [main])
AC_SUBST(HAVE_LIBREADLINE)

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
#   AC_MSG_RESULT(from environment: ${BLAS})
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
#   AC_MSG_RESULT(fallback to gslcblas)

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

PKG_CHECK_MODULES([M4RI],[m4ri],,AC_MSG_ERROR([no m4ri config found]))
M4RI_CFLAGS+=" -std=c99"
AC_SUBST([M4RI_CFLAGS])

AC_SUBST(BLAS, ${blas})
AC_SUBST(BLAS2, ${blas2})

# ouch?
my_CPPFLAGS+=' -I$(top_srcdir)/..'
AC_SUBST([my_CPPFLAGS])

# more paths
c_lib_include='$(top_srcdir)/../c_lib/include'
CSAGE_INCLUDES=-I$c_lib_include
AC_SUBST(C_LIB_INCLUDE, $c_lib_include)
AC_SUBST(CSAGE_INCLUDES)

# fixme: use AC_...
numpy_include_dir=$sage_local/lib/python/site-packages/numpy/core/include
NUMPY_INCLUDES=-I$numpy_include_dir
AC_SUBST(numpy_include_dir)
AC_SUBST(NUMPY_INCLUDES)

SAGE_INC=$sage_local/include
AC_SUBST(SAGE_INC)

SAGE_DIR=$srcdir
AC_SUBST(SAGE_DIR)

AS_AC_EXPAND(SAGE_ETC, $sysconfdir)

# additional packages
AS_IF([test -d $sage_local/share/conway_polynomials],
      [CONWAY_DATA_DIR=$sage_local/share/conway_polynomials],
      [test -d /usr/share/sagemath/conway_polynomials],
      [CONWAY_DATA_DIR=/usr/share/sagemath/conway_polynomials],
      [CONWAY_DATA_DIR=/usr/share/conway_polynomials])
AC_SUBST([CONWAY_DATA_DIR])
AM_SUBST_NOTMAKE([CONWAY_DATA_DIR])

AS_IF([test -d $sage_local/share/graphs],
      [GRAPHS_DATA_DIR=$sage_local/share/graphs],
      [test -d /usr/share/sagemath/graphs],
      [GRAPHS_DATA_DIR=/usr/share/sagemath/graphs],
      [AC_MSG_ERROR([cannot find graphs database])])
AC_SUBST([GRAPHS_DATA_DIR])
AM_SUBST_NOTMAKE([GRAPHS_DATA_DIR])

AS_IF([test -d $sage_local/share/reflexive_polytopes],
      [POLYTOPE_DATA_DIR=$sage_local/share/reflexive_polytopes],
      [test -d /usr/share/sagemath/reflexive_polytopes],
      [POLYTOPE_DATA_DIR=/usr/share/sagemath/reflexive_polytopes],
      [AC_MSG_ERROR([cannot find polytopes database])])
AC_SUBST([POLYTOPE_DATA_DIR])
AM_SUBST_NOTMAKE([POLYTOPE_DATA_DIR])

AS_IF([test -d $sage_local/share/ellvurves],
      [ELLCURVE_DATA_DIR=$sage_local/share/ellcurves],
      [test -d /usr/share/sagemath/ellcurves],
      [ELLCURVE_DATA_DIR=/usr/share/sagemath/ellcurves],
      [AC_MSG_ERROR([cannot find elliptic curves])])
AC_SUBST([ELLCURVE_DATA_DIR])
AM_SUBST_NOTMAKE([ELLCURVE_DATA_DIR])

m4ri_extra_compile_args=
AC_SUBST(m4ri_extra_compile_args)

# output files

AC_CONFIG_FILES([
    setup.py
    module_list.py
    Makefile
    algebras/letterplace/Makefile
    algebras/Makefile
    algebras/quatalg/Makefile
    calculus/Makefile
    categories/examples/Makefile
    categories/Makefile
    coding/Makefile
    combinat/Makefile
    combinat/matrices/Makefile
    combinat/words/Makefile
    crypto/Makefile
    databases/Makefile
    doctest/Makefile
    ext/interpreters/Makefile
    ext/Makefile
    finance/Makefile
    functions/Makefile
    games/Makefile
    geometry/Makefile
    geometry/triangulation/Makefile
    graphs/base/Makefile
    graphs/graph_decompositions/Makefile
    graphs/Makefile
    graphs/modular_decomposition/Makefile
    groups/abelian_gps/Makefile
    groups/Makefile
    groups/matrix_gps/Makefile
    groups/perm_gps/Makefile
    groups/perm_gps/partn_ref/Makefile
    gsl/Makefile
    homology/Makefile
    interacts/Makefile
    interfaces/Makefile
    lfunctions/Makefile
    libs/coxeter3/Makefile
    libs/cremona/Makefile
    libs/flint/Makefile
    libs/fplll/Makefile
    libs/gap/Makefile
    libs/lcalc/Makefile
    libs/lrcalc/Makefile
    libs/linbox/Makefile
    libs/Makefile
    libs/mpmath/Makefile
    libs/mwrank/Makefile
    libs/ntl/Makefile
    libs/pari/Makefile
    libs/singular/Makefile
    libs/symmetrica/Makefile
    logic/Makefile
    matrix/Makefile
    media/Makefile
    misc/Makefile
    modular/Makefile
    modular/arithgroup/Makefile
    modular/modform/Makefile
    modular/modsym/Makefile
    modules/fg_pid/Makefile
    modules/Makefile
    monoids/Makefile
    numerical/backends/Makefile
    numerical/Makefile
    parallel/Makefile
    plot/Makefile
    plot/plot3d/Makefile
    probability/Makefile
    quadratic_forms/Makefile
    rings/finite_rings/Makefile
    rings/function_field/Makefile
    rings/Makefile
    rings/number_field/Makefile
    rings/padics/Makefile
    rings/polynomial/Makefile
    rings/polynomial/padics/Makefile
    rings/semirings/Makefile
    rings/universal_cyclotomic_field/Makefile
    sandpiles/Makefile
    sat/Makefile
    sat/solvers/cryptominisat/Makefile
    sat/solvers/Makefile
    schemes/elliptic_curves/Makefile
    schemes/hyperelliptic_curves/Makefile
    schemes/Makefile
    schemes/toric/Makefile
    server/Makefile
    server/notebook/Makefile
    sets/Makefile
    stats/hmm/Makefile
    stats/Makefile
    structure/Makefile
    structure/proof/Makefile
    symbolic/integration/Makefile
    symbolic/Makefile
    tensor/Makefile
    tests/Makefile
    env.py
])

# create dummy files for cython file dependencies
# (this is currently not natively supported by automake)
AC_CONFIG_COMMANDS([cythondep],
                   [$ac_top_srcdir/cythondep AMDEP_TRUE=$AMDEP_TRUE])

AC_CONFIG_FILES([cythoninit],[chmod +x cythoninit])
AC_CONFIG_COMMANDS([cython_init],
                   [./cythoninit])

AC_SUBST(PYTHONPATH)

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
   PYTHON:     $PYTHON
])

# vim:et:sw=2:
