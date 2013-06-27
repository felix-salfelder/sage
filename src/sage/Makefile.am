# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
ACLOCAL_AMFLAGS = -Im4

# FIXME: fallback to setup.py if desired
SUBDIRS = \
    algebras calculus categories coding combinat crypto databases ext finance functions games geometry \
    graphs groups gsl homology \
    interfaces interacts libs lfunctions logic \
    matrix media misc modular modules monoids numerical \
    parallel plot probability quadratic_forms rings sandpiles \
    schemes sets stats structure symbolic tensor tests server doctest sat

sagedir = $(pythondir)/sage
sage_PYTHON = \
    all_cmdline.py \
    all_notebook.py \
    __init__.py \
    version.py \
    env.py \
    all.py

# FIXME: move to post_commands?
@VPATH_TRUE@all: | __init__.py
@VPATH_TRUE@__init__.py:
@VPATH_TRUE@	touch $@

# this implements the currently
# unavaible AM_EXTRA_RECURSIVE_TARGETS, see common.mk
py: @VPATH_TRUE@pys
	for i in $(SUBDIRS); do $(MAKE) -C $$i $@; done

pyall: .
	( cd $(VPATH); find . -name '*.py' )| sort > $@

PYS = $(filter %.py,$(DIST_COMMON))
pycheck: pyall
	echo $(PYS) | tr ' ' '\n' | sed 's#^#@abs_builddir@/#' | \
	      sed 's#^@abs_top_builddir@#.#' > pyreg
	for i in $(SUBDIRS); do $(MAKE) -C $$i $@ PYLIST=../pyreg; done
	sort pyreg > pyregs; mv pyregs pyreg
	diff -d pyreg pyall | tee pydiff; exit $${PIPESTATUS[0]}
	rm pyreg pyall pydiff



if VPATH_BUILD
pys:
	for i in $(filter_out env.py, $(sage_PYTHON)); \
		do cp -p @srcdir@/$$i .; done
PHONYPYS = pys
endif

# manually implementing AM_EXTRA_RECURSIVE_TARGETS([py])
# this will be in automake1.12 (?)
.PHONY: py $(PHONYPYS)
