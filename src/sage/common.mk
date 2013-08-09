# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
# this file helps working around automake limitations
# eventually it can be removed, after
# - all default values are moved to configure.ac
# - automake supports cython
#   - dependencies
#   - vpath quirks
# - automake supports AM_RECURSIVE_TARGETS
#

# this is stupid, intended to approximate distutils.
# see http://www.gnu.org/software/automake/manual/html_node/Wildcards.html
#
#allpythonstuff = $(wildcard *.py *.pxd *.pxi)

AM_LDFLAGS = -module -avoid-version -L@top_builddir@/../c_lib/src/.libs
AM_CPPFLAGS = @my_CPPFLAGS@

# how to do this right? LDADD?
AM_LDFLAGS+= -L@top_builddir@/../c_lib/src/.libs

# user specified MAKEFLAGS
# AM_CPPFLAGS += $(CPPFLAGS)

# just append globally, needed quite often.
AM_CPPFLAGS += @CSAGE_INCLUDES@

# this is the directory that contains "sage"
AM_CPPFLAGS += -I$(abs_top_srcdir)/..

# FIXME: place where required (partly done)
LIBS += -lcsage

# dont spam terminal with error messages
CYTHONFLAGS = --fast-fail

# write cython_debug
# does not work. workdir must be @srcdir@
# CYTHON_GDBOPT = --gdb
CYTHON_GDBOPT = --gdb-outdir @abs_top_builddir@/..
if CYGDB
CYTHONFLAGS += $(CYTHON_GDBOPT)
endif

# this is required for inspection
CYTHONFLAGS += --embed-positions

# sage still relies on ...
CYTHONFLAGS += --old-style-globals

# more switches
CYTHONFLAGS += -X autotestdict=False
CYTHONFLAGS += -X cdivision=True
CYTHONFLAGS += -X fast_getattr=True

# problem: include paths...
CYTHONFLAGS += -I$(abs_top_srcdir)/.. -I$(abs_top_builddir)/..

# should look like this (but doesn't)
CYTHONFLAGS += -I$(abs_top_srcdir) -I$(abs_top_builddir)

CYTHON ?= cython

# needed to force correct paths in docstrings
# wrong paths lead to mysterious sageinspect.py errors
CYTHON_WORKING = -w $(abs_top_srcdir)/..
CYTHONFLAGS += $(CYTHON_WORKING)

# not necessary? non-VPATH build untested.
# if VPATH_BUILD
# CYTHON_EXTRA_PATH =
# else
# CYTHON_EXTRA_PATH = $(abs_builddir)/
# endif

AM_V_CYT = $(am__v_CYT_$(V))
am__v_CYT_ = $(am__v_CYT_$(AM_DEFAULT_VERBOSITY))
am__v_CYT_0 = @echo "  CYTH  " $@;

AM_V_PYC = $(am__v_PYC_$(V))
am__v_PYC_ = $(am__v_PYC_$(AM_DEFAULT_VERBOSITY))
am__v_PYC_0 = @echo "  PYC   " $@;

AM_V_PYO = $(am__v_PYO_$(V))
am__v_PYO_ = $(am__v_PYO_$(AM_DEFAULT_VERBOSITY))
am__v_PYO_0 = @echo "  PYO   " $@;

# ouch, trailing colon triggers python bug: empty string will be misinterpreted
# as '.'.
PYTHONPATHENV = PYTHONPATH="@abs_top_builddir@/..$(PYTHONPATH:%=:%)"

define cython_call
	$(AM_V_CYT)$(PYTHONPATHENV) $(CYTHON) $(CYTHONFLAGS) $(abspath $(CYTHON_EXTRA_PATH)$<) \
	    -o $(abs_builddir)/$@ @AMDEP_TRUE@@PYDEP_TRUE@-MD -MP
	@AMDEP_TRUE@@PYDEP_TRUE@$(AM_V_at)mv $@.d $(DEPDIR)/$*.Pcython
endef

%.cc: CYTHONFLAGS+=--cplus

MANUAL_DEP_PYS=$(filter %.pyx %.pyxx,$(SOURCES))
MANUAL_DEP_PYX=$(MANUAL_DEP_PYS:%.pyxx=%.pyx)
MANUAL_DEP=$(MANUAL_DEP_PYX:%.pyx=$(DEPDIR)/%.Pcython)

CLEANFILES = $(MANUAL_DEP_PYX:%.pyx=%.c) \
             $(MANUAL_DEP_PYX:%.pyx=%.cc) \
             *.so *.pyc *.pyo

@AMDEP_TRUE@ifneq (,$(MANUAL_DEP))
@AMDEP_TRUE@@am__include@ $(DEPDIR)/*.Pcython
@AMDEP_TRUE@endif

.pyx.c:
	$(cython_call)
.pyxx.cc:
	$(cython_call)

PYS = $(filter %.py,$(DIST_COMMON))
PYCS = $(PYS:%.py=%.pyc)
PYOS = $(PYS:%.py=%.pyo)

py-local: $(LTLIBRARIES:%.la=%.so) $(PYCS) $(PYOS)
	
# FIXME: V
$(LTLIBRARIES:%.la=%.so): %.so: | %.la
	-$(LN_S) .libs/$@ .

# this is probably nonsense
# @VPATH_TRUE@pys: $(PYS)
# @VPATH_TRUE@	for i in $(PYS); do \
# @VPATH_TRUE@	    mkdir -p `dirname $$i`; \
# @VPATH_TRUE@	    cp @srcdir@/$$i $$i; \
# @VPATH_TRUE@	done
# @VPATH_TRUE@.PHONY: pys

# manually implementing AM_EXTRA_RECURSIVE_TARGETS([py pycheck])
# will be implemented in automake1.12
py: py-local py-recursive
py-recursive:
	for i in $(SUBDIRS); do $(MAKE) -C $$i py || exit 1; done
pycheck: pycheck-local pycheck-recursive
pycheck-recursive:
	for i in $(SUBDIRS); do $(MAKE) -C $$i pycheck PYLIST=../$(PYLIST); done

@am__leading_dot@PHONY: py-recursive py-local py \
                        pycheck-recursive pycheck-local pycheck

PYLIST=none

# compare registered .py's against existing
pycheck-local:
	echo $(PYS) | tr ' ' '\n' | sed 's#^#@abs_builddir@/#' | \
	      sed 's#^@abs_top_builddir@#.#' >> $(PYLIST)

# this won't work as long as _PYTHON includes subdirectories
# @diff <(echo "$(PYS)" | tr ' ' '\n' | sort) <(cd $(VPATH); ls *.py | sort)

#don't delete .cc .c just because gcc fails.
@am__leading_dot@PRECIOUS: %.cc %.c

# yes, this is ugly, may be replaced with make 3.82
%.pyc: SHELL=/usr/bin/env bash
%.pyo: SHELL=/usr/bin/env bash
%.pyc: %.py
	@VPATH_TRUE@@$(MKDIR_P) $(dir $@)
	$(AM_V_PYC)echo -e 'import py_compile\npy_compile.compile("$<","$@")' | $(PYTHON) -
%.pyo: %.py
	@VPATH_TRUE@@$(MKDIR_P) $(dir $@)
	$(AM_V_PYO)echo -e 'import py_compile\npy_compile.compile("$<","$@")' | $(PYTHON) -O -
