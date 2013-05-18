SUBDIRS = calculus categories coding combinat crypto ext finance functions games geometry graphs groups gsl interacts libs matrix media misc modules numerical parallel plot quadratic_forms rings sets stats structure symbolic tests

ACLOCAL_AMFLAGS = -Im4

py: @VPATH_TRUE@pys
	for i in $(SUBDIRS); do $(MAKE) -C $$i py; done

@VPATH_TRUE@pys:
	cp -p @srcdir@/__init__.py .

# manually implementing AM_EXTRA_RECURSIVE_TARGETS([py])
@am__leading_dot@PHONY: py
@VPATH_TRUE@@am__leading_dot@PHONY: pys
