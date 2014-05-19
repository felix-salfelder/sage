# this file is part of Sage
# (c) 2013-14 Felix Salfelder
# license: gplv3+
#
include $(top_srcdir)/common.mk
inst_PYTHON = \
    all.py \
    interpreter.py \
    __init__.py \
    ipython_extension.py

AM_DEFAULT_SOURCE_EXT = .pyx
inst_LTLIBRARIES = \
    inputhook.la \
    readline_extra_commands.la

inputhook_la_LIBADD = @CSAGE_LIBS@
readline_extra_commands_la_LIBADD = -lreadline
