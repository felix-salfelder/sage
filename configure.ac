#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([sage], [5.9-autotools], [sage-devel@googlegroups.com])
AM_INIT_AUTOMAKE([-Wall -Werror -Wno-portability silent-rules])
AC_CONFIG_SRCDIR([README])
AC_CONFIG_MACRO_DIR([m4])

# `pwd` resolves $abs_top_builddir
# abs_top_builddir is not available here.
AC_PREFIX_DEFAULT(`pwd`/local)

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AC_PROG_CPP
AC_PROG_FC       # FIXME: not required, just check.
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AC_PROG_GREP     # required to build singular
AC_PROG_SED      # used here and there.

# install GCC when needed.
# FIXME: override this (former SAGE_INSTALL_GCC environment)
CHK_gcc=positive

# Check whether $CC is some version of GCC.  If it's a different
# compiler, install GCC locally.
# CCtype=`testcc.sh $CC`
if test ! "$CC" = gcc; then
  AC_MSG_NOTICE([Installing GCC because your '$CC' isn't GCC (GNU CC) but $CC.])
  CHK_gcc=negative
else
  # $CC points to some version of GCC, find out which version.
  GCCVERSION=`$CC -dumpversion`
  case $GCCVERSION in
      [0-3].*|4.[0-3]|4.[0-3].*)
          # Install our own GCC if the system-provided one is older than gcc-4.4.
          # * gcc-4.2.4 compiles a slow IML:
          # https://groups.google.com/forum/?fromgroups#!topic/sage-devel/Ux3t0dW2FSI
          # * gcc-4.3 might have trouble building ATLAS:
          # https://groups.google.com/forum/?fromgroups#!topic/sage-devel/KCeFqQ_w2FE
          AC_MSG_NOTICE([Installing GCC because you have $CC version $GCCVERSION, which is quite old.])
          CHK_gcc=negative;;
      4.4*|4.5*)
          # GCC 4.4.x and GCC 4.5.x fail to compile PARI/GP on ia64:
          # * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46044
          if test x`uname -m` = xia64; then
              AC_MSG_NOTICE([Installing GCC because you have $CC version $GCCVERSION on ia64.])
              AC_MSG_NOTICE([gcc <= 4.5 fails to compile PARI/GP on ia64.])
              CHK_gcc=negative
          fi;;
      4.6.[01])
          # Also install GCC if we have version 4.6.0 or 4.6.1, which is
          # known to give trouble within Sage:
          # * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48702
          # * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48774
          AC_MSG_NOTICE([Installing GCC because you have $CC version $GCCVERSION.])
          AC_MSG_NOTICE([gcc-4.6.0 and gcc-4.6.1 have known bugs affecting Sage.])
          CHK_gcc=negative;;
      4.6*)
          # GCC 4.6.x doesn't compile ECL on Cygwin:
          # * http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061
          if uname | grep CYGWIN >/dev/null; then
              AC_MSG_NOTICE([Installing GCC because you have $CC version $GCCVERSION on Cygwin.])
              AC_MSG_NOTICE([gcc-4.6.x fails to compile ECL on Cygwin.])
              CHK_gcc=negative
          fi;;
      4.7.0)
          # GCC 4.7.0 is very broken on ia64, see
          # http://gcc.gnu.org/bugzilla/show_bug.cgi?id=48496
          # This is fixed in GCC 4.7.1.
          if test x`uname -m` = xia64; then
              AC_MSG_NOTICE([Installing GCC because you have $CC version $GCCVERSION on ia64.])
              AC_MSG_NOTICE([gcc-4.7.0 has a serious bug on ia64.])
              CHK_gcc=negative
          fi;;
  esac
fi

# try to guess SAGE_* stuff
sage_local=$prefix
if test "x$prefix" = xNONE; then
    sage_local=$ac_default_prefix
else
    AC_MSG_ERROR([custom prefix is not implementable yet.])
fi

AC_SUBST(SAGE_LOCAL, $sage_local)

# Check C++ and Fortran compilers.
if test -z "$CXX"; then
  echo >&2 "Installing GCC because a C++ compiler is missing."
  need_to_install_gcc=yes
fi

if test -z "$FC"; then
  echo >&2 "Installing GCC because a Fortran compiler is missing."
  need_to_install_gcc=yes
fi

if test "$need_to_install_gcc" = yes -o -x "$sage_local/bin/gfortran"; then
    FC=gfortran
    unset SAGE_FORTRAN_LIB
fi

# FIXME: what is this trying to implement?
# (it's deprecated anyway)
# Make the fortran library symlink if requested
#if [ -f "$SAGE_FORTRAN_LIB" ]; then
#    ( cd "$SAGE_LOCAL/lib" && ln -sf "$SAGE_FORTRAN_LIB" . )
#fi

AC_MSG_CHECKING(GNU tar)
AC_PATH_PROGS_FEATURE_CHECK(
  [TAR], [tar gtar],
  [[tarout=`$ac_path_TAR --version 2>&1 | grep GNU`
    test -n "$tarout" && ac_cv_path_TAR=$ac_path_TAR ac_path_TAR_found=:]],
  [ AC_MSG_RESULT([no]);
    AC_MSG_ERROR([could not find GNU tar])
  ]
)
AC_MSG_RESULT([$ac_cv_path_TAR])
AC_SUBST([TAR], [$ac_cv_path_TAR])

AC_MSG_CHECKING(GNU make)
AC_PATH_PROGS_FEATURE_CHECK(
  [GMAKE], [make gmake],
  [[makeout=`$ac_path_GMAKE --version 2>&1 | grep GNU`
    test -n "$makeout" && ac_cv_path_GMAKE=$ac_path_GMAKE ac_path_GMAKE_found=:]],
  [ AC_MSG_RESULT([no]);
    AC_MSG_ERROR([could not find GNU make])
  ]
)
AC_MSG_RESULT([$ac_cv_path_GMAKE])
AC_SUBST([GMAKE], [$ac_cv_path_GMAKE])

# download tool (to make dist*)

# (FIXME, later)
AC_SUBST(URL_GRABBER, "wget -c")
AC_SUBST(DOWNLOAD_URL, "http://www.sagemath.org/packages/upstream")
AC_SUBST(UPSTREAM, upstream)

# SAGE_ROOT contains .BUILDSTART, so it must translate to $abs_top_builddir
# and $abs_top_builddir is just `pwd`
AC_SUBST(SAGE_ROOT, `pwd`)

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_TYPE_UID_T
AC_C_INLINE
AC_TYPE_MODE_T
AC_TYPE_OFF_T
AC_TYPE_PID_T
AC_C_RESTRICT
AC_TYPE_SIZE_T
AC_CHECK_MEMBERS([struct stat.st_blksize])
AC_STRUCT_ST_BLOCKS
AC_CHECK_MEMBERS([struct stat.st_rdev])
AC_TYPE_UINT32_T

# Checks for library functions.
AC_FUNC_ALLOCA
AC_FUNC_CHOWN
AC_FUNC_ERROR_AT_LINE
AC_FUNC_FORK
AC_FUNC_LSTAT_FOLLOWS_SLASHED_SYMLINK
AC_FUNC_MALLOC
AC_FUNC_MKTIME
AC_FUNC_REALLOC
AC_CHECK_FUNCS([endgrent endpwent floor getcwd inet_ntoa memset mkdir pathconf setenv sqrt strchr strdup strstr uname utime])

## sage foreign package in/exclusion
# base packages
# checks for packages
AC_MSG_CHECKING([whether iconv is required])
case "$UNAME" in
    CYGWIN|HP-UX|SunOS)
        AC_MSG_RESULT([yes])
        CHK_iconv=negative
        ;;
    *)
        AC_MSG_RESULT([no])
        CHK_iconv=positive
        ;;
esac

AC_ARG_VAR([FOREIGN_DEFAULT])
FOREIGN_DEFAULT=${FOREIGN_DEFAULT:-auto}

FOREIGN_AVAILABLE=
FOREIGN_DISABLED=
FOREIGN_ENABLED=

AC_FOREIGN_PACKAGE([atlas])
AC_FOREIGN_PACKAGE([cliquer])
AC_FOREIGN_PACKAGE([blas])
AC_FOREIGN_PACKAGE([boehm_gc])
AC_FOREIGN_PACKAGE([boost_cropped])
AC_FOREIGN_PACKAGE([cddlib])
AC_FOREIGN_PACKAGE([cephes])
AC_FOREIGN_PACKAGE([cliquer])
AC_FOREIGN_PACKAGE([conway_polynomials])
AC_FOREIGN_PACKAGE([cvxopt])
AC_FOREIGN_PACKAGE([cython])
AC_FOREIGN_PACKAGE([docutils])
AC_FOREIGN_PACKAGE([ecl])
AC_FOREIGN_PACKAGE([eclib])
AC_FOREIGN_PACKAGE([ecm])
AC_FOREIGN_PACKAGE([elliptic_curves])
AC_FOREIGN_PACKAGE([fflas_ffpack])
AC_FOREIGN_PACKAGE([flint])
AC_FOREIGN_PACKAGE([flintqs])
AC_FOREIGN_PACKAGE([libfplll])
AC_FOREIGN_PACKAGE([freetype])
AC_FOREIGN_PACKAGE([genus2reduction])
AC_FOREIGN_PACKAGE([gap])
AC_FOREIGN_PACKAGE([gcc])
AC_FOREIGN_PACKAGE([gd])
AC_FOREIGN_PACKAGE([gdmodule])
AC_FOREIGN_PACKAGE([gfan])
AC_FOREIGN_PACKAGE([givaro])
AC_FOREIGN_PACKAGE([git])
AC_FOREIGN_PACKAGE([glpk])
AC_FOREIGN_PACKAGE([graphs])
AC_FOREIGN_PACKAGE([gsl])
AC_FOREIGN_PACKAGE([iconv])
AC_FOREIGN_PACKAGE([iml])
AC_FOREIGN_PACKAGE([ipython])
AC_FOREIGN_PACKAGE([jinja2])
AC_FOREIGN_PACKAGE([jmol])
AC_FOREIGN_PACKAGE([lapack])
AC_FOREIGN_PACKAGE([lcalc])
AC_FOREIGN_PACKAGE([lrcalc])
AC_FOREIGN_PACKAGE([libgap])
AC_FOREIGN_PACKAGE([libpng])
AC_FOREIGN_PACKAGE([linbox])
AC_FOREIGN_PACKAGE([libm4ri])
AC_FOREIGN_PACKAGE([libm4rie])
AC_FOREIGN_PACKAGE([matplotlib])
AC_FOREIGN_PACKAGE([maxima])
AC_FOREIGN_PACKAGE([mpc])
AC_FOREIGN_PACKAGE([mpfi])
AC_FOREIGN_PACKAGE([mpfr])
AC_FOREIGN_PACKAGE([mpir])
AC_FOREIGN_PACKAGE([mpmath])
AC_FOREIGN_PACKAGE([networkx])
AC_FOREIGN_PACKAGE([ntl])
AC_FOREIGN_PACKAGE([numpy])
AC_FOREIGN_PACKAGE([palp])
AC_FOREIGN_PACKAGE([pari])
AC_FOREIGN_PACKAGE([pexpect])
AC_FOREIGN_PACKAGE([pil])
AC_FOREIGN_PACKAGE([polybori])
AC_FOREIGN_PACKAGE([polytopes_db])
AC_FOREIGN_PACKAGE([ppl])
AC_FOREIGN_PACKAGE([pycrypto])
AC_FOREIGN_PACKAGE([pygments])
AC_FOREIGN_PACKAGE([pynac])
AC_FOREIGN_PACKAGE([python])
AC_FOREIGN_PACKAGE([ratpoints])
AC_FOREIGN_PACKAGE([r])
AC_FOREIGN_PACKAGE([rpy2])
AC_FOREIGN_PACKAGE([readline])
AC_FOREIGN_PACKAGE([rubiks])
AC_FOREIGN_PACKAGE([sagenb])
AC_FOREIGN_PACKAGE([sagetex])
AC_FOREIGN_PACKAGE([scipy])
AC_FOREIGN_PACKAGE([scons])
AC_FOREIGN_PACKAGE([setuptools])
AC_FOREIGN_PACKAGE([singular])
AC_FOREIGN_PACKAGE([sphinx])
AC_FOREIGN_PACKAGE([sqlalchemy])
AC_FOREIGN_PACKAGE([sqlite])
AC_FOREIGN_PACKAGE([symmetrica])
AC_FOREIGN_PACKAGE([sympow])
AC_FOREIGN_PACKAGE([sympy])
AC_FOREIGN_PACKAGE([tachyon])
AC_FOREIGN_PACKAGE([termcap])
AC_FOREIGN_PACKAGE([zlib])
AC_FOREIGN_PACKAGE([znpoly])

# include submodules in dist tarball
distdir_subs='distdir: DIST_SUBDIRS+=$(CORE_MODULES)'
AC_SUBST([distdir_subs])
AM_SUBST_NOTMAKE([distdir_subs])

# misc
dotPRECIOUS='.PRECIOUS'
AC_SUBST([dotPRECIOUS])
AM_SUBST_NOTMAKE([dotPRECIOUS])
AC_SUBST(UNAME, `uname`)

AC_CONFIG_FILES([GNUmakefile
                 deps
                 dist/spkg.mk
                 dist/bin/Makefile
                 dist/Makefile
                 dist/etc/env.sh])

AC_CONFIG_FILES([dist/bin/sage-dist-install],
       [chmod +x dist/bin/sage-dist-install])
AC_CONFIG_FILES([dist/bin/sage-dist-make],
       [chmod +x dist/bin/sage-dist-make])
AC_CONFIG_FILES([dist/bin/sage_fortran],
       [chmod +x dist/bin/sage_fortran])

# this is currently not needed.
AC_CONFIG_FILES([sage],
       [chmod +x sage])

# not a good idea. packages are not installed yet.
# AC_CONFIG_SUBDIRS([src/bin])

AC_OUTPUT

if test $FOREIGN_DEFAULT = yes; then
   packageinfo="installing all packages"
   if test -n "$FOREIGN_DISABLED"; then
      packageinfo+=" except$FOREIGN_DISABLED"
   fi
elif test $FOREIGN_DEFAULT = no; then
   packageinfo="installing no foreign packages"
   if test -n "$FOREIGN_ENABLED"; then
      packageinfo+=" except$FOREIGN_ENABLED"
   fi
else
   packageinfo="classic (automatic) mode"
   if test -n "$FOREIGN_AVAILABLE"; then
      packageinfo+=", unnecessary:$FOREIGN_AVAILABLE"
   fi
   if test -n "$FOREIGN_DISABLED"; then
      packageinfo+=", also skipping$FOREIGN_DISABLED"
   fi
   if test -n "$FOREIGN_ENABLED"; then
      packageinfo+=", installing anyway$FOREIGN_ENABLED"
   fi
fi

AC_MSG_RESULT([
** Configuration summary for $PACKAGE $VERSION:

   prefix:     $prefix
   $packageinfo
])

# vim:et
