# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#

install-data-local: docbuild

all: docbuild

EXTRA_DIST = common $(LANGDIRS)
LANGDIRS = de en fr ru tr
	
# hmm better build env?

docbuild: common/builder.py common/build_options.py
	for i in $(LANGDIRS); do $(MKDIR_P) $$i/reference; done
	export SAGE_DOC="@abs_top_builddir@"; \
	export SAGE_DOC_SRC="@abs_top_srcdir@"; \
	export SAGE_SRC="@abs_top_srcdir@/.."; \
	export DOT_SAGE="$$( mktemp -d )"; \
	export PATH="@abs_top_srcdir@/../bin:$$PATH"; \
	export SAGE_MAXIMA_INIT="@abs_top_srcdir@/../bin/sage-maxima.lisp"; \
	export LD_LIBRARY_PATH="@abs_top_builddir@/../c_lib/src/.libs"; \
	export PYTHONPATH=common:$$PYTHONPATH:@abs_top_builddir@/..:@abs_top_srcdir@; \
	$(PYTHON) $< --no-pdf-links all html; \
	rm -r $$DOT_SAGE

install-data-local:
	$(INSTALL) -d $(docdir)
	cp -r output/* $(docdir)


docenvconfdir=$(sysconfdir)/env.d
docenvconf_DATA = doc.sh

.PHONY: docbuild
