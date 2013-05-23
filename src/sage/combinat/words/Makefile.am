SUBDIRS =
include $(top_srcdir)/common.mk
combinat_wordsdir = $(pythondir)/sage/combinat/words
combinat_words_PYTHON = __init__.py abstract_word.py all.py alphabet.py finite_word.py infinite_word.py morphism.py paths.py shuffle_product.py suffix_trees.py word.py word_generators.py word_infinite_datatypes.py word_options.py words.py
combinat_words_LTLIBRARIES = word_datatypes.la 
word_datatypes_la_LIBADD =
word_datatypes.cc: @srcdir@/word_datatypes.pyx
word_datatypes_la_CPPFLAGS = -Isage/combinat/words $(AM_CPPFLAGS)
.pyx.cc:
	$(cython_call)
