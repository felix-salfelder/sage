# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
# CWD is supposed to be the package root containing the upstream source in "src"
#
# !! this is untested/sketchy !! (but it works)

# SAGE_LOCAL = @SAGE_LOCAL@
# SAGE_PREFIX = @SAGE_PREFIX@
SAGE_ETC = $(SAGE_LOCAL)/etc

ifneq ($(FILELIST),)
FILELIST_ARG = --record '$(FILELIST)'
endif

ifneq ($(DESTDIR),)
DESTDIR_ARG = -D '$(DESTDIR)'
DESTDIR_SET = DESTDIR="$(DESTDIR)"
endif

# distutils call
SETUP_PY_INSTALL = $(DESTDIR_SET) sage-setup.py install $(FILELIST_ARG)

# install wrapped
SAGE_INSTALL = sage-dist-install
#$(FILELIST_ARG)
SAGE_INSTALLDIRS = $(SAGE_INSTALL) -d

## workaround
# use these if upstream dishonours DESTDIR
SAGE_INSTALL_DESTDIR = $(SAGE_INSTALL) $(DESTDIR_ARG)
SAGE_INSTALLDIRS_DESTDIR = $(SAGE_INSTALL) $(DESTDIR_ARG) -d

all: check install

check: spkg-check

# run spkg-check if it exists
spkg-check: build
	[ ! -x spkg-check ] || ./spkg-check

.PHONY: spkg-check

install: tmpclean patch-stamp

unpatch:
	if test -f patch-stamp; then \
		echo unpatch not implemented yet. delete with make clean if necessary; \
	fi

SRC=src

# Apply all patches
# hmm, some more magic?
patch-stamp: # | patches
	@: > $@.T
	@for patch in $(sort $(wildcard patches/*.patch)); do \
	    [ -r "$$patch" ] || continue; \
	    patch -d $(SRC) -p1 < "$$patch"; \
	    if [ $$? -ne 0 ]; then \
	        echo >&2 "Error applying '$$patch'"; \
	        exit 1; \
	    fi; \
	    echo $$patch >> $@.T; \
	done
	@mv $@.T $@


installtmp: DESTDIR=`pwd`/tmp
installtmp: install
binary: installtmp
	cd tmp; tar -cjf ../sage-bin-$(PACKAGE).tar.bz2
source: distclean patch-stamp
	cd src; tar -cjf ../sage-src-$(PACKAGE).tar.bz2

# hmm, this will be different from package to package
distclean:

tmpclean:
	rm -rf tmp

.PHONY: configure unpatch build install check binary tmpclean distclean
