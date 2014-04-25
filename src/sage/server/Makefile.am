# this file is part of Sage
# (c) 2013 Felix Salfelder
# license: gplv3+
#
SUBDIRS = notebook
include $(top_srcdir)/common.mk

inst_PYTHON = \
    all.py __init__.py \
    misc.py \
    nodoctest.py support.py

server_tracdir = $(instdir)/trac
server_trac_PYTHON = \
    trac/all.py \
    trac/__init__.py \
    trac/trac.py
