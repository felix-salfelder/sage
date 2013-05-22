#!/bin/sh
ACLOCAL_FLAGS=-Im4

libtoolize
aclocal $ACLOCAL_FLAGS
autoconf
automake --add-missing

for i in $( find . -name Makefile.am ); do
	a=${i%.am}; b=${a#./}
	echo "/bin/sh missing --run automake-1.11 $b"
	/bin/sh missing --run automake-1.11 $b
done
