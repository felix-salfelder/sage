dnl a macro to register foreigns.
dnl dnl  AC_FOREIGN_PACKAGE([name])
dnl
AC_DEFUN([AC_FOREIGN_PACKAGE],
 [AC_ARG_ENABLE([$1], AS_HELP_STRING([--enable-$1], [Build $1]),
 [case "${enableval}" in
  yes) $1=true ;;
  no)  $1=false ;;
  *) AC_MSG_ERROR([bad value ${enableval} for --enable-$1]) ;;
 esac],[$1=$FOREIGN_DEFAULT])
 our_package='$(INST)/$(FP_$1)'
 if test $$1 = auto; then
  # automatic == classic mode
  if test x$CHK_$1 = xpositive; then
   # we are quite sure that the system package is okay, don't depend on ours.
   FOREIGN_AVAILABLE+=" $1"
   DEP_$1=
   $1=no
  else
   DEP_$1=$our_package
   $1=yes
  fi
 elif test $$1 = true; then
  FOREIGN_ENABLED+=" $1"
  if test x$CHK_$1 = xpositive; then
   AC_MSG_NOTICE(["forcefully overriding available system package: $1"])
  fi
  DEP_$1=$our_package
 else # --disable-<packagename>
  FOREIGN_DISABLED+=" $1"
  if test x$CHK_$1 = xnegative; then
   AC_MSG_NOTICE([system package for $1 is known to not work. you have been warned!])
   sleep 3
  fi
 fi
 AC_SUBST(DEP_$1)
 m4_pushdef([uppercase],translit([[$1]],[a-z],[A-Z]))

 # this is not currently used. might be helpful...
 AM_CONDITIONAL([SAGE_OWN_]uppercase, [test x$$1 = xtrue])
 m4_popdef([uppercase])
 ])
