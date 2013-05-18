#!/bin/sh
ACLOCAL_FLAGS=-Im4

libtoolize
aclocal $ACLOCAL_FLAGS
autoconf
automake --add-missing
