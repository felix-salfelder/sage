r"""
Skew Tableaux
"""
#*****************************************************************************
#       Copyright (C) 2007 Mike Hansen <mhansen@gmail.com>,
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.rings.all import Integer, QQ, ZZ
from sage.misc.misc import uniq
from sage.functions.all import factorial
from sage.matrix.all import zero_matrix
import partition
import sage.combinat.tableau
import skew_partition
import partition
import copy
from combinat import CombinatorialObject, CombinatorialClass, InfiniteAbstractCombinatorialClass
from integer_vector import IntegerVectors
from sage.combinat.words.words import Words

def SkewTableau(st=None, expr=None):
    """
    Returns the skew tableau object corresponding to st.

    Note that Sage uses the English convention for partitions and
    tableaux.

    EXAMPLES::

        sage: st = SkewTableau([[None, 1],[2,3]]); st
        [[None, 1], [2, 3]]
        sage: st.inner_shape()
        [1]
        sage: st.outer_shape()
        [2, 2]

    The expr form of a skew tableau consists of the inner partition
    followed by a list of the entries in row from bottom to top.

    ::

        sage: SkewTableau(expr=[[1,1],[[5],[3,4],[1,2]]])
        [[None, 1, 2], [None, 3, 4], [5]]
    """
    if isinstance(st, SkewTableau_class):
        return st

    if expr is not None:
        return from_expr(expr)

    for row in st:
        if not isinstance(row, list):
            raise TypeError, "each element of the skew tableau must be a list"
        if row == []:
            raise TypeError, "a skew tableau cannot have an empty list for a row"

    return SkewTableau_class(st)

class SkewTableau_class(CombinatorialObject):
    def __init__(self, t):
        """
        TESTS::

            sage: st = SkewTableau([[None, 1],[2,3]])
            sage: st == loads(dumps(st))
            True
        """
        CombinatorialObject.__init__(self,t)

    def _repr_diagram(self):
        """
        Return a string representation of ``self`` as a diagram.

        EXAMPLES::

            sage: print SkewTableau([[None,2,3],[None,4],[5]])._repr_diagram()
              .  2  3
              .  4
              5
        """
        none_str = lambda x: "  ." if x is None else "%3s"%str(x)
        new_rows = ["".join(map(none_str, row)) for row in self]
        return '\n'.join(new_rows)

    def pp(self):
        """
        Return a pretty print string of the tableau.

        EXAMPLES::

            sage: SkewTableau([[None,2,3],[None,4],[5]]).pp()
              .  2  3
              .  4
              5
        """
        print self._repr_diagram()

    def _ascii_art_(self):
        """
        TESTS::

            sage: ascii_art(RibbonTableaux([[2,1],[]],[1,1,1],1).list())
            [   1  3    1  2 ]
            [   2   ,   3    ]
        """
        from sage.misc.ascii_art import AsciiArt
        return AsciiArt(self._repr_diagram().splitlines())

    def outer_shape(self):
        """
        Returns the outer shape of the tableau.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).outer_shape()
            [3, 2, 1]
        """

        return partition.Partition([len(row) for row in self])


    def inner_shape(self):
        """
        Returns the inner shape of the tableau.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).inner_shape()
            [1, 1]
        """

        return partition.Partition(filter(lambda x: x != 0, [len(filter(lambda x: x is None, row)) for row in self]))

    def shape(self):
        r"""
        Returns the shape of a tableau t.

        EXAMPLES::

            sage: SkewTableau([[None,1,2],[None,3],[4]]).shape()
            [[3, 2, 1], [1, 1]]
        """

        return skew_partition.SkewPartition([self.outer_shape(), self.inner_shape()])


    def outer_size(self):
        """
        Returns the size of the outer shape of the skew tableau.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).outer_size()
            6
            sage: SkewTableau([[None, 2], [1, 3]]).outer_size()
            4
        """
        return self.outer_shape().size()



    def inner_size(self):
        """
        Returns the size of the inner shape of the skew tableau.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).inner_size()
            2
            sage: SkewTableau([[None, 2], [1, 3]]).inner_size()
            1
        """
        return self.inner_shape().size()

    def size(self):
        """
        Returns the number of cells in the skew tableau.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 4], [None, 3], [1]]).size()
            4
            sage: SkewTableau([[None, 2], [1, 3]]).size()
            3
        """
        return sum([len(filter(lambda x: x is not None,row)) for row in self])



    def conjugate(self):
        """
        Returns the conjugate of the skew tableau.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]]).conjugate()
            [[None, 2], [1, 3]]
        """
        conj_shape = self.outer_shape().conjugate()

        conj = [[None]*row_length for row_length in conj_shape]

        for i in range(len(conj)):
            for j in range(len(conj[i])):
                conj[i][j] = self[j][i]


        return SkewTableau(conj)


    def to_word_by_row(self):
        """
        Returns a word obtained from a row reading of the skew tableau.

        EXAMPLES::

            sage: s = SkewTableau([[None,1],[2,3]])
            sage: s.pp()
              .  1
              2  3
            sage: s.to_word_by_row()
            word: 231
            sage: s = SkewTableau([[None, 2, 4], [None, 3], [1]])
            sage: s.pp()
              .  2  4
              .  3
              1
            sage: s.to_word_by_row()
            word: 1324

        TESTS::

            sage: SkewTableau([[None, None, None], [None]]).to_word_by_row()
            word:
            sage: SkewTableau([]).to_word_by_row()
            word:
        """
        word = []
        for row in self:
            word = row + word

        return Words("positive integers")([i for i in word if i is not None])


    def to_word_by_column(self):
        """
        Returns the word obtained from a column reading of the skew
        tableau

        EXAMPLES::

            sage: s = SkewTableau([[None,1],[2,3]])
            sage: s.pp()
              .  1
              2  3
            sage: s.to_word_by_column()
            word: 132

        ::

            sage: s = SkewTableau([[None, 2, 4], [None, 3], [1]])
            sage: s.pp()
            .  2  4
            .  3
            1
            sage: s.to_word_by_column()
            word: 4231
        """
        return self.conjugate().to_word_by_row()

    to_word = to_word_by_row

    def to_permutation(self):
        """
        Return a permutation with the entries of ``self`` obtained by reading
        ``self`` row by row, from the bottommost to the topmost row, with
        each row being read from left to right, in English convention.
        See :meth:`to_word_by_row()`.

        EXAMPLES::

            sage: SkewTableau([[None,2],[3,4],[None],[1]]).to_permutation()
            [1, 3, 4, 2]
            sage: SkewTableau([[None]]).to_permutation()
            []
        """
        from sage.combinat.permutation import Permutation
        return Permutation(self.to_word())

    def evaluation(self):
        """
        Returns the evaluation of the word from skew tableau.

        EXAMPLES::

            sage: SkewTableau([[1,2],[3,4]]).evaluation()
            [1, 1, 1, 1]
        """
        ed = self.to_word().evaluation_dict()
        entries = ed.keys()
        m = max(entries) + 1 if entries else -1
        return [ed.get(k,0) for k in range(1,m)]

    weight = evaluation

    def is_standard(self):
        """
        Returns True if self is a standard skew tableau and False
        otherwise.

        EXAMPLES::

            sage: SkewTableau([[None, 2], [1, 3]]).is_standard()
            True
            sage: SkewTableau([[None, 2], [2, 4]]).is_standard()
            False
            sage: SkewTableau([[None, 3], [2, 4]]).is_standard()
            False
            sage: SkewTableau([[None, 2], [2, 4]]).is_standard()
            False
        """
        #Check to make sure that it is filled with 1...size
        w = self.to_word()
        if sorted(w) != range(1, self.size()+1):
            return False
        else:
            return self.is_semistandard()

    def is_semistandard(self):
        """
        Returns True if self is a semistandard skew tableau and False
        otherwise.

        EXAMPLES::

            sage: SkewTableau([[None, 2, 2], [1, 3]]).is_semistandard()
            True
            sage: SkewTableau([[None, 2], [2, 4]]).is_semistandard()
            True
            sage: SkewTableau([[None, 3], [2, 4]]).is_semistandard()
            True
            sage: SkewTableau([[None, 2], [1, 2]]).is_semistandard()
            False
        """
        t = self

        #Check to make sure it is weakly increasing along the rows
        for row in t:
            for i in range(1, len(row)):
                if row[i-1] is not None and row[i] < row[i-1]:
                    return False


        #Check to make sure it is strictly increasing along the columns
        conj = t.conjugate()
        for row in conj:
            for i in range(1, len(row)):
                if row[i-1] is not None and row[i] <= row[i-1]:
                    return False

        return True

    def to_tableau(self):
        """
        Returns a tableau with the same filling. This only works if the
        inner shape of the skew tableau has size zero.

        EXAMPLES::

            sage: SkewTableau([[1,2],[3,4]]).to_tableau()
            [[1, 2], [3, 4]]
        """

        if self.inner_size() != 0:
            raise ValueError, "the inner size of the skew tableau must be 0"
        else:
            return  sage.combinat.tableau.Tableau(self[:])

    def restrict(self, n):
        """
        Returns the restriction of the (semi)standard skew tableau to all
        the numbers less than or equal to n.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2],[3]]).restrict(2)
            [[None, 1], [2]]
            sage: SkewTableau([[None,1],[2],[3]]).restrict(1)
            [[None, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).restrict(1)
            [[None, 1], [1]]
        """
        t = self[:]
        return SkewTableau( filter(lambda z: z != [], map(lambda x: filter(lambda y: y is None or y <= n, x), t)) )

    def to_chain(self):
        """
        Returns the chain of partitions corresponding to the (semi)standard
        skew tableau.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2],[3]]).to_chain()
            [[1], [2], [2, 1], [2, 1, 1]]
            sage: SkewTableau([[None,1],[1],[2]]).to_chain()
            [[1], [2, 1], [2, 1, 1]]
        """
        weights = [0] + uniq(sorted(self.to_word()))
        return [ self.restrict(x).shape()[0] for x in weights]

    def slide(self, corner=None):
        """
        Jeu-de-taquin slide

        Apply a jeu-de-taquin slide to self on the specified corner and returns the new tableau.
        If no corner is given an arbitrary corner is chosen.

        Fulton, William. 'Young Tableaux'. p12-13

        EXAMPLES::

            sage: st = SkewTableau([[None, None, None, None,2],[None, None, None, None,6], [None, 2, 4, 4], [2, 3, 6], [5,5]])
            sage: st.slide((2,0))
            [[None, None, None, None, 2], [None, None, None, None, 6], [2, 2, 4, 4], [3, 5, 6], [5]]

        TESTS::

            sage: st
            [[None, None, None, None, 2], [None, None, None, None, 6], [None, 2, 4, 4], [2, 3, 6], [5, 5]]
        """
        new_st = [x[:] for x in self]
        inner_corners = self.inner_shape().corners()
        outer_corners = self.outer_shape().corners()
        if corner is not None:
            if tuple(corner) not in inner_corners:
                raise ValueError, "corner must be an inner corner"
        else:
            if len(inner_corners) == 0:
                return self
            else:
                corner = inner_corners[0]

        spotl, spotc = corner
        while (spotl, spotc) not in outer_corners:
            #print spot
            #Check to see if there is nothing to the right
            if spotc == len(new_st[spotl]) - 1:
                #print "nr"
                #Swap the hole with the cell below
                new_st[spotl][spotc] = new_st[spotl+1][spotc]
                new_st[spotl+1][spotc] = None
                spotl += 1
                continue

            #Check to see if there is nothing below
            if (spotl == len(new_st) - 1) or (len(new_st[spotl+1]) <= spotc):
                #print "nb"
                #Swap the hole with the cell to the right
                new_st[spotl][spotc] = new_st[spotl][spotc+1]
                new_st[spotl][spotc+1] = None
                spotc += 1
                continue

            #If we get to this stage, we need to compare
            below = new_st[spotl+1][spotc]
            right = new_st[spotl][spotc+1]
            if below <= right:
                #Swap with the cell below
                #print "b"
                new_st[spotl][spotc] = new_st[spotl+1][spotc]
                new_st[spotl+1][spotc] = None
                spotl += 1
                continue
            else:
                #Swap with the cell to the right
                #print "r"
                new_st[spotl][spotc] = new_st[spotl][spotc+1]
                new_st[spotl][spotc+1] = None
                spotc += 1
                continue

        #Clean up to remove the "None" at an outside corner
        #Remove the last row if there is nothing left in it
        new_st[spotl].pop()
        if len(new_st[spotl]) == 0:
            new_st.pop()

        return SkewTableau(new_st)


    def rectify(self):
        """
        Returns a Tableau formed by applying the jeu de taquin process to
        self.

        Fulton, William. 'Young Tableaux'. p15

        EXAMPLES::

            sage: s = SkewTableau([[None,1],[2,3]])
            sage: s.rectify()
            [[1, 3], [2]]
            sage: SkewTableau([[None, None, None, 4],[None,None,1,6],[None,None,5],[2,3]]).rectify()
            [[1, 3, 4, 6], [2, 5]]

        TESTS::

            sage: s
            [[None, 1], [2, 3]]
        """
        rect = copy.deepcopy(self)
        inner_corners = rect.inner_shape().corners()

        while len(inner_corners) > 0:
            rect = rect.slide()
            inner_corners = rect.inner_shape().corners()

        return rect.to_tableau()

    def standardization(self, check=True):
        r"""
        Return the standardization of ``self``, assuming ``self`` is a
        semistandard skew tableau.

        The standardization of a semistandard skew tableau `T` is the standard
        skew tableau `\mathrm{st}(T)` of the same shape as `T` whose
        reversed reading word is the standardization of the reversed reading
        word of `T`.

        The standardization of a word `w` can be formed by replacing all `1`'s
        in `w` by `1, 2, \ldots, k_1` from left to right, all `2`'s in `w` by
        `k_1 + 1, k_1 + 2, \ldots, k_2`, and repeating for all letters that
        appear in `w`.
        See also :meth:`Word.standard_permutation()`.

        INPUT:

        - ``check`` -- (Default: ``True``) Check to make sure ``self`` is
          semistandard. Set to ``False`` to avoid this check.

        EXAMPLES::

            sage: t = SkewTableau([[None,None,3,4,7,19],[None,4,4,8],[None,5,16,17],[None],[2],[3]])
            sage: t.standardization()
            [[None, None, 3, 6, 8, 12], [None, 4, 5, 9], [None, 7, 10, 11], [None], [1], [2]]

        Standard skew tableaux are fixed under standardization::

            sage: p = Partition([4,3,3,2])
            sage: q = Partitions(3).random_element()
            sage: all((t == t.standardization() for t in StandardSkewTableaux([p, q])))
            True

        The reading word of the standardization is the
        standardization of the reading word::

            sage: t = SkewTableau([[None,3,4,4],[None,6,10],[7,7,11],[18]])
            sage: t.to_word().standard_permutation() == t.standardization().to_permutation()
            True

        TESTS:

        Some corner cases::

            sage: t = SkewTableau([[None,None],[None]])
            sage: t.standardization()
            [[None, None], [None]]
            sage: t = SkewTableau([])
            sage: t.standardization()
            []
        """
        if check and not self.is_semistandard():
            raise ValueError("the skew tableau must be semistandard")
        # This should be a SkewStandardTableau
        return from_shape_and_word(self.shape(), self.to_word_by_row().standard_permutation())

    def bender_knuth_involution(self, k, rows=None, check=True):
        r"""
        Return the image of ``self`` under the `k`-th Bender--Knuth
        involution, assuming ``self`` is a skew semistandard tableau.

        Let `T` be a tableau, then a *lower free `k` in `T`* means a cell of
        `T` which is filled with the integer `k` and whose direct lower
        neighbor is not filled with the integer `k + 1` (in particular,
        this lower neighbor might not exist at all). Let an *upper free `k + 1`
        in `T`* mean a cell of `T` which is filled with the integer `k + 1`
        and whose direct upper neighbor is not filled with the integer `k`
        (in particular, this neighbor might not exist at all). It is clear
        that for any row `r` of `T`, the lower free `k`'s and the upper
        free `k + 1`'s in `r` together form a contiguous interval or `r`.

        The *`k`-th Bender--Knuth switch at row `i`* changes the entries of
        the cells in this interval in such a way that if it used to have
        `a` entries of `k` and `b` entries of `k + 1`, it will now
        have `b` entries of `k` and `a` entries of `k + 1`. For fixed `k`, the
        `k`-th Bender--Knuth switches for different `i` commute. The
        composition of the `k`-th Bender--Knuth switches for all rows is
        called the *`k`-th Bender--Knuth involution*. This is used to show that
        the Schur functions defined by semistandard (skew) tableaux are
        symmetric functions.

        INPUT:

        - ``k`` -- an integer

        - ``rows`` -- (Default ``None``) When set to ``None``, the method
          computes the `k`-th Bender--Knuth involution as defined above.
          When an iterable, this computes the composition of the `k`-th
          Bender--Knuth switches at row `i` over all `i` in ``rows``. When set
          to an integer `i`, the method computes the `k`-th Bender--Knuth
          switch at row `i`. Note the indexing of the rows starts with `1`.

        - ``check`` -- (Default: ``True``) Check to make sure ``self`` is
          semistandard. Set to ``False`` to avoid this check.

        OUTPUT:

        The image of ``self`` under either the `k`-th Bender--Knuth
        involution, the `k`-th Bender--Knuth switch at a certain row, or
        the composition of such switches, as detailed in the INPUT section.

        EXAMPLES::

            sage: t = SkewTableau([[None,None,None,4,4,5,6,7],[None,2,4,6,7,7,7],[None,4,5,8,8,9],[None,6,7,10],[None,8,8,11],[None],[4]])
            sage: t
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7], [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(1)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 1, 4, 6, 7, 7, 7], [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(4)
            [[None, None, None, 4, 5, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7], [None, 5, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [5]]
            sage: t.bender_knuth_involution(5)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 5, 7, 7, 7], [None, 4, 6, 8, 8, 9], [None, 5, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(6)
            [[None, None, None, 4, 4, 5, 6, 6], [None, 2, 4, 6, 6, 7, 7], [None, 4, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]
            sage: t.bender_knuth_involution(666) == t
            True
            sage: t.bender_knuth_involution(4, 2) == t
            True
            sage: t.bender_knuth_involution(4, 3)
            [[None, None, None, 4, 4, 5, 6, 7], [None, 2, 4, 6, 7, 7, 7], [None, 5, 5, 8, 8, 9], [None, 6, 7, 10], [None, 8, 8, 11], [None], [4]]

        The Bender--Knuth involution is an involution::

            sage: t = SkewTableau([[None,3,4,4],[None,6,10],[7,7,11],[18]])
            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(k) == t for k in range(1,4))
            True

        The same for the single switches::

            sage: all(t.bender_knuth_involution(k, j).bender_knuth_involution(k, j) == t for k in range(1,5) for j in range(1, 5))
            True

        Locality of the Bender--Knuth involutions::

            sage: all(t.bender_knuth_involution(k).bender_knuth_involution(l) == t.bender_knuth_involution(l).bender_knuth_involution(k) for k in range(1,5) for l in range(1,5) if abs(k - l) > 1)
            True

        Coxeter relation of the Bender--Knuth involutions (they have the form
        `(ab)^6 = 1`)::

            sage: p = lambda t, k: t.bender_knuth_involution(k).bender_knuth_involution(k + 1)
            sage: all(p(p(p(p(p(p(t,k),k),k),k),k),k) == t for k in range(1,5))
            True

        TESTS::

            sage: t = SkewTableau([])
            sage: t.bender_knuth_involution(3)
            []
            sage: t = SkewTableau([[None,None],[None]])
            sage: t.bender_knuth_involution(3)
            [[None, None], [None]]

        AUTHORS:

        - Darij Grinberg (2013-05-14)
        """
        if check and not self.is_semistandard():
            raise ValueError("the skew tableau must be semistandard")
        l = len(self)    # l is the number of rows of self.
        # Sanitizing the rows input so that it always becomes a list of
        # nonnegative integers. We also subtract 1 from these integers
        # because the i-th row of a tableau T is T[i - 1].
        if rows is None:
            rows = range(l)
        elif rows in ZZ:
            rows = [rows - 1]
        else:
            rows = [i - 1 for i in rows]
        # Now, rows should be iterable.

        # result_tab is going to be the result tableau (as a list of lists);
        # we will build it up step by step, starting with a deep copy of self.
        result_tab = [row[:] for row in self]
        for i in rows:
            if i >= l:
                continue
            # Setup the previous and next rows
            if i == 0:
                prev_row = [None] * len(result_tab[i])
            else:
                prev_row = result_tab[i-1]
            if i == l - 1:
                next_row = [None] * len(result_tab[i])
            else:
                next_row = result_tab[i+1] + [None] * (len(result_tab[i]) - len(result_tab[i+1]))
            a = 0
            b = 0
            sk = None # The first entry of k
            sk1 = None # The first entry of k+1
            for j, val in enumerate(result_tab[i]):
                if val == k and next_row[j] != k + 1:
                    if sk is None:
                        sk = j
                    a += 1
                elif val == k + 1 and prev_row[j] != k:
                    if sk1 is None:
                        sk1 = j
                    b += 1
            if sk1 is not None:
                if a > b:
                    for j in range(sk1-(a-b), sk1):
                        result_tab[i][j] = k + 1
                elif a < b:
                    for j in range(sk1, sk1+b-a):
                        result_tab[i][j] = k
            elif sk is not None:
                for j in range(sk, sk+a):
                    result_tab[i][j] = k + 1

        return SkewTableau(result_tab) # This should be a SkewSemistandardTableau

    def to_expr(self):
        """
        The first list in a result corresponds to the inner partition of
        the skew shape. The second list is a list of the rows in the skew
        tableau read from the bottom up.

        Provided for compatibility with MuPAD-Combinat. In MuPAD-Combinat,
        if t is a skew tableau, then to_expr gives the same result as
        expr(t) would give in MuPAD-Combinat.

        EXAMPLES::

            sage: SkewTableau([[None,1,1,3],[None,2,2],[1]]).to_expr()
            [[1, 1], [[1], [2, 2], [1, 1, 3]]]
            sage: SkewTableau([]).to_expr()
            [[], []]
        """
        rows = self.filling()
        rows.reverse()
        return [self.inner_shape(), rows]


    def is_ribbon(self):
        """
        Returns True if and only if self is a ribbon, that is if it has no
        2x2 boxes.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]]).is_ribbon()
            True
            sage: SkewTableau([[None,1,2],[3,4,5]]).is_ribbon()
            False
        """
        outer = list(self.outer_shape())
        inner = list(self.inner_shape())
        inner += [0]*(len(outer)-len(inner))

        for i in range(1, len(outer)):
            if outer[i] > inner[i-1]+1:
                return False

        return True

    def to_ribbon(self):
        """
        Returns the ribbon version of self.

        EXAMPLES::

            sage: SkewTableau([[None,1],[2,3]]).to_ribbon()
            [[1], [2, 3]]
        """
        if not self.is_ribbon():
            raise ValueError, "self must be a ribbon"
        import ribbon
        r =  [ [i for i in row if i is not None] for row in self]
        return ribbon.Ribbon_class(r)


    def filling(self):
        """
        Returns a list of the non-empty entries in self.

        EXAMPLES::

            sage: t = SkewTableau([[None,1],[2,3]])
            sage: t.filling()
            [[1], [2, 3]]
        """
        return [ [i for i in row if i is not None] for row in self ]

    def cells_by_content(self, c):
        """
        Returns the coordinates of the cells in self with content c.

        ::

            sage: s = SkewTableau([[None,1,2],[3,4,5],[6]])
            sage: s.cells_by_content(0)
            [(1, 1)]
            sage: s.cells_by_content(1)
            [(0, 1), (1, 2)]
            sage: s.cells_by_content(2)
            [(0, 2)]
            sage: s.cells_by_content(-1)
            [(1, 0)]
            sage: s.cells_by_content(-2)
            [(2, 0)]
        """
        if len(self) == 0:
            return []

        if c >= 0:
            if c >= len(self[0]):
                return []
            i,j = 0,c
        else:
            c = -c
            if c >= len(self):
                return []
            i,j = c,0

        res = []
        while True:
            if self[i][j] is not None:
                res.append((i,j))
            i,j = i+1, j+1
            if i >= len(self) or j >= len(self[i]):
                break
        return res

    def entries_by_content(self, c):
        """
        Returns on the entries in self with content c.

        EXAMPLES::

            sage: s = SkewTableau([[None,1,2],[3,4,5],[6]])
            sage: s.entries_by_content(0)
            [4]
            sage: s.entries_by_content(1)
            [1, 5]
            sage: s.entries_by_content(2)
            [2]
            sage: s.entries_by_content(-1)
            [3]
            sage: s.entries_by_content(-2)
            [6]
        """
        return [self[i][j] for i,j in self.cells_by_content(c)]

    def cells(self):
        """
        Returns the cells in self.

        EXAMPLES::

            sage: s = SkewTableau([[None,1,2],[3],[6]])
            sage: s.cells()
            [(0, 1), (0, 2), (1, 0), (2, 0)]
        """
        res = []
        for i in range(len(self)):
            for j in range(len(self[i])):
                if self[i][j] is not None:
                    res.append( (i,j) )
        return res



def _label_skew(list, sk):
    """
    Returns a filled in a standard skew tableaux given an ordered list
    of the coordinates to filled in.

    EXAMPLES::

        sage: import sage.combinat.skew_tableau as skew_tableau
        sage: l = [ '0,0', '1,1', '1,0', '0,1' ]
        sage: empty = [[None,None],[None,None]]
        sage: skew_tableau._label_skew(l, empty)
        [[1, 4], [3, 2]]
    """
    i = 1
    skew = copy.deepcopy(sk)
    for coordstring in list:
            coords = coordstring.split(",")
            row = int(coords[0])
            column = int(coords[1])
            skew[row][column] = i
            i += 1
    return skew

def StandardSkewTableaux(skp=None):
    """
    Returns the combinatorial class of standard skew tableaux of shape
    skp (where skp is a skew partition).

    EXAMPLES::

        sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).list()
        [[[None, 1, 2], [None, 3], [4]],
         [[None, 1, 2], [None, 4], [3]],
         [[None, 1, 3], [None, 2], [4]],
         [[None, 1, 4], [None, 2], [3]],
         [[None, 1, 3], [None, 4], [2]],
         [[None, 1, 4], [None, 3], [2]],
         [[None, 2, 3], [None, 4], [1]],
         [[None, 2, 4], [None, 3], [1]]]
    """
    if skp is None:
        return StandardSkewTableaux_all()
    elif isinstance(skp, (int, Integer)):
        return StandardSkewTableaux_size(skp)
    elif skp in skew_partition.SkewPartitions():
        return StandardSkewTableaux_skewpartition(skew_partition.SkewPartition(skp))
    else:
        raise TypeError

class StandardSkewTableaux_all(InfiniteAbstractCombinatorialClass):
    def __repr__(self):
        """
        EXAMPLES::

            sage: StandardSkewTableaux() #indirect doctest
            Standard skew tableaux
        """
        return "Standard skew tableaux"

    def __contains__(self, x):
        """
        EXAMPLES::

            sage: [[None, 2], [1, 3]] in StandardSkewTableaux()
            True
            sage: [[None, 2], [2, 4]] in StandardSkewTableaux()
            False
            sage: [[None, 3], [2, 4]] in StandardSkewTableaux()
            False
            sage: [[None, 2], [2, 4]] in StandardSkewTableaux()
            False
        """
        if isinstance(x, SkewTableau_class):
            return True

        try:
            x = SkewTableau(x)
        except TypeError:
            return False

        return x.is_standard()

    def _infinite_cclass_slice(self, n):
        """
        Needed by InfiniteAbstractCombinatorialClass to build __iter__.

        TESTS::

            sage: StandardSkewTableaux()._infinite_cclass_slice(4) == StandardSkewTableaux(4)
            True
            sage: it = iter(StandardSkewTableaux())    # indirect doctest
            sage: [it.next() for i in range(10)]
            [[], [[1]], [[1, 2]], [[1], [2]], [[None, 1], [2]], [[None, 2], [1]], [[1, 2, 3]], [[1, 2], [3]], [[1, 3], [2]], [[None, 1, 2], [3]]]
        """
        return StandardSkewTableaux_size(n)


class StandardSkewTableaux_size(CombinatorialClass):
    def __init__(self, n):
        """
        EXAMPLES::

            sage: s = StandardSkewTableaux(3)
            sage: s == loads(dumps(s))
            True
        """
        self.n = n

    def __repr__(self):
        """
        EXAMPLES::

            sage: StandardSkewTableaux(3) #indirect doctest
            Standard skew tableaux of size 3
        """
        return "Standard skew tableaux of size %s"%self.n

    def cardinality(self):
        """
        EXAMPLES::

            sage: StandardSkewTableaux(1).cardinality()
            1
            sage: StandardSkewTableaux(2).cardinality()
            4
            sage: StandardSkewTableaux(3).cardinality()
            24
            sage: StandardSkewTableaux(4).cardinality()
            194
        """
        count = 0
        for skp in skew_partition.SkewPartitions(self.n):
            count += StandardSkewTableaux_skewpartition(skp).cardinality()
        return count

    def __iter__(self):
        """
        EXAMPLES::

            sage: StandardSkewTableaux(2).list() #indirect doctest
            [[[1, 2]], [[1], [2]], [[None, 1], [2]], [[None, 2], [1]]]

            sage: StandardSkewTableaux(3).list() #indirect doctest
            [[[1, 2, 3]],
             [[1, 2], [3]], [[1, 3], [2]],
             [[None, 1, 2], [3]], [[None, 1, 3], [2]],
             [[None, 2, 3], [1]],
             [[None, 1], [2, 3]], [[None, 2], [1, 3]],
             [[None, None, 1], [2, 3]], [[None, None, 2], [1, 3]], [[None, None, 3], [1, 2]],
             [[1], [2], [3]],
             [[None, 1], [None, 2], [3]], [[None, 1], [None, 3], [2]], [[None, 2], [None, 3], [1]],
             [[None, 1], [2], [3]], [[None, 2], [1], [3]], [[None, 3], [1], [2]],
             [[None, None, 1], [None, 2], [3]], [[None, None, 1], [None, 3], [2]],
             [[None, None, 2], [None, 1], [3]], [[None, None, 3], [None, 1], [2]],
             [[None, None, 2], [None, 3], [1]], [[None, None, 3], [None, 2], [1]]]
        """
        for skp in skew_partition.SkewPartitions(self.n):
            for sst in StandardSkewTableaux_skewpartition(skp):
                yield sst

class StandardSkewTableaux_skewpartition(CombinatorialClass):
    Element = SkewTableau_class
    def __init__(self, skp):
        """
        TESTS::

            sage: S = StandardSkewTableaux([[3, 2, 1], [1, 1]])
            sage: S == loads(dumps(S))
            True
        """
        self.skp = skp

    def list(self):
        """
        Returns a list for all the standard skew tableaux with shape of the
        skew partition skp. The standard skew tableaux are ordered
        lexicographically by the word obtained from their row reading.

        EXAMPLES::

            sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).list()
            [[[None, 1, 2], [None, 3], [4]],
             [[None, 1, 2], [None, 4], [3]],
             [[None, 1, 3], [None, 2], [4]],
             [[None, 1, 4], [None, 2], [3]],
             [[None, 1, 3], [None, 4], [2]],
             [[None, 1, 4], [None, 3], [2]],
             [[None, 2, 3], [None, 4], [1]],
             [[None, 2, 4], [None, 3], [1]]]
        """
        return [st for st in self]

    def cardinality(self):
        """
        Returns the number of standard skew tableaux with shape of the skew
        partition skp.  This uses a formula due to Aitken
        (see Cor. 7.16.3 of [Sta1999]_).

        EXAMPLES::

            sage: StandardSkewTableaux([[3, 2, 1], [1, 1]]).cardinality()
            8
        """
        outer, inner = self.skp
        m = len(outer)
        n = sum(outer) - sum(inner)
        outer = list(outer)
        inner = list(inner) + [0]*(m-len(inner))
        a = zero_matrix(QQ, m)
        for i in range(m):
            for j in range(m):
                v = outer[i] - inner[j] - i + j
                if v < 0:
                    a[i,j] = 0
                else:
                    a[i,j] = 1/factorial(v)
        return ZZ(factorial(n) * a.det())

    def __iter__(self):
        """
        An iterator for all the standard skew tableau with shape of the
        skew partition skp. The standard skew tableaux are ordered
        lexicographically by the word obtained from their row reading.

        EXAMPLES::

            sage: [st for st in StandardSkewTableaux([[3, 2, 1], [1, 1]])] # indirect doctest
            [[[None, 1, 2], [None, 3], [4]],
             [[None, 1, 2], [None, 4], [3]],
             [[None, 1, 3], [None, 2], [4]],
             [[None, 1, 4], [None, 2], [3]],
             [[None, 1, 3], [None, 4], [2]],
             [[None, 1, 4], [None, 3], [2]],
             [[None, 2, 3], [None, 4], [1]],
             [[None, 2, 4], [None, 3], [1]]]
        """
        skp = self.skp

        dag = skp.to_dag()
        le_list = list(dag.topological_sort_generator())

        empty = [[None]*row_length for row_length in skp.outer()]

        for le in le_list:
            yield SkewTableau(_label_skew(le, empty))


def SemistandardSkewTableaux(p=None, mu=None):
    """
    Returns a combinatorial class of semistandard skew tableaux.

    EXAMPLES::

        sage: SemistandardSkewTableaux()
        Semistandard skew tableaux

    ::

        sage: SemistandardSkewTableaux(3)
        Semistandard skew tableaux of size 3

    ::

        sage: SemistandardSkewTableaux([[2,1],[]])
        Semistandard skew tableaux of shape [[2, 1], []]

    ::

        sage: SemistandardSkewTableaux([[2,1],[]],[2,1])
        Semistandard skew tableaux of shape [[2, 1], []] and weight [2, 1]

    ::

        sage: SemistandardSkewTableaux(3, [2,1])
        Semistandard skew tableaux of size 3 and weight [2, 1]
    """
    if p is None and mu is None:
        return SemistandardSkewTableaux_all()

    if p is None:
        raise ValueError, "you must specify either a size or shape"

    if isinstance(p, (int, Integer)):
        if mu is None:
            return SemistandardSkewTableaux_size(p)
        else:
            return SemistandardSkewTableaux_size_weight(p, mu)

    if p in skew_partition.SkewPartitions():
        p = skew_partition.SkewPartition(p)
        if mu is None:
            return SemistandardSkewTableaux_shape(p)
        else:
            return SemistandardSkewTableaux_shape_weight(p, mu)



class SemistandardSkewTableaux_all(CombinatorialClass):
    def __repr__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux().__repr__()
            'Semistandard skew tableaux'
        """
        return "Semistandard skew tableaux"

class SemistandardSkewTableaux_size(CombinatorialClass):
    def __init__(self, n):
        """
        EXAMPLES::

            sage: s = SemistandardSkewTableaux(3)
            sage: s == loads(dumps(s))
            True
        """
        self.n = n

    def __repr__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(3).__repr__()
            'Semistandard skew tableaux of size 3'
        """
        return "Semistandard skew tableaux of size %s"%self.n

    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2).cardinality()
            8
        """
        count = 0
        for p in skew_partition.SkewPartitions(self.n):
            count += SemistandardSkewTableaux_shape(p).cardinality()
        return count

    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2).list() # indirect doctest
            [[[1, 1]],
             [[1, 2]],
             [[2, 2]],
             [[1], [2]],
             [[None, 1], [1]],
             [[None, 2], [1]],
             [[None, 1], [2]],
             [[None, 2], [2]]]
        """
        for p in skew_partition.SkewPartitions(self.n):
            for ssst in SemistandardSkewTableaux_shape(p):
                yield ssst

class SemistandardSkewTableaux_size_weight(CombinatorialClass):
    def __init__(self, n, mu):
        """
        EXAMPLES::

            sage: s = SemistandardSkewTableaux(3,[2,1])
            sage: s == loads(dumps(s))
            True
        """
        self.n = n
        self.mu = mu

    def __repr__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(3,[2,1]).__repr__()
            'Semistandard skew tableaux of size 3 and weight [2, 1]'
        """
        return "Semistandard skew tableaux of size %s and weight %s"%(self.n,self.mu)

    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2,[1,1]).cardinality()
            4
        """
        count = 0
        for p in skew_partition.SkewPartitions(self.n):
            count += SemistandardSkewTableaux_shape_weight(p, self.mu).cardinality()
        return count

    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux(2,[1,1]).list() # indirect doctest
            [[[1, 2]], [[1], [2]], [[None, 2], [1]], [[None, 1], [2]]]
        """
        for p in skew_partition.SkewPartitions(self.n):
            for ssst in SemistandardSkewTableaux_shape_weight(p, self.mu):
                yield ssst

class SemistandardSkewTableaux_shape(CombinatorialClass):
    def __init__(self, p):
        """
        EXAMPLES::

            sage: s = SemistandardSkewTableaux([[2,1],[]])
            sage: s == loads(dumps(s))
            True
        """
        self.p = skew_partition.SkewPartition(p)

    def __repr__(self):
        """
        EXAMPLES::

            sage: repr(SemistandardSkewTableaux([[2,1],[]]))
            'Semistandard skew tableaux of shape [[2, 1], []]'
        """
        return "Semistandard skew tableaux of shape %s"%self.p

    def cardinality(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]]).cardinality()
            8
        """
        count = 0
        for mu in IntegerVectors(self.p.size(), self.p.size()):
            count += SemistandardSkewTableaux_shape_weight(self.p, mu).cardinality()
        return count

    def __iter__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]]).list() #indirect test
            [[[1, 1], [2]],
             [[1, 1], [3]],
             [[1, 2], [2]],
             [[1, 3], [2]],
             [[1, 2], [3]],
             [[1, 3], [3]],
             [[2, 2], [3]],
             [[2, 3], [3]]]
        """
        for mu in IntegerVectors(self.p.size(), self.p.size()):
            for ssst in SemistandardSkewTableaux_shape_weight(self.p, mu):
                yield ssst

class SemistandardSkewTableaux_shape_weight(CombinatorialClass):
    def __init__(self, p, mu):
        """
        EXAMPLES::

            sage: s = SemistandardSkewTableaux([[2,1],[]],[2,1])
            sage: s == loads(dumps(s))
            True
        """
        self.p = p
        self.mu = mu

    def __repr__(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]],[2,1]).__repr__()
            'Semistandard skew tableaux of shape [[2, 1], []] and weight [2, 1]'
        """
        return "Semistandard skew tableaux of shape %s and weight %s"%(self.p, self.mu)


    def list(self):
        """
        EXAMPLES::

            sage: SemistandardSkewTableaux([[2,1],[]],[2,1]).list()
            [[[1, 1], [2]]]
        """
        import ribbon_tableau
        res = ribbon_tableau.RibbonTableaux_shapeweightlength(self.p, self.mu, 1).list()
        return [ SkewTableau_class(x._list) for x in res]


def from_expr(expr):
    """
    Returns a SkewTableau from a MuPAD-Combinat expr for a skew
    tableau. The first list in expr is the inner shape of the skew
    tableau. The second list are the entries in the rows of the skew
    tableau from bottom to top.

    Provided primarily for compatibility with MuPAD-Combinat.

    EXAMPLES::

        sage: import sage.combinat.skew_tableau as skew_tableau
        sage: sage.combinat.skew_tableau.from_expr([[1,1],[[5],[3,4],[1,2]]])
        [[None, 1, 2], [None, 3, 4], [5]]
    """
    skp = []
    outer = expr[1]
    inner = expr[0]+[0]*(len(outer)-len(expr[0]))

    for i in range(len(outer)):
        skp.append( [None]*(inner[i]) + outer[-(i+1)] )

    return SkewTableau(skp)



def from_shape_and_word(shape, word):
    """
    Returns the skew tableau corresponding to the skew partition shape
    and the word obtained from the row reading.

    EXAMPLES::

        sage: import sage.combinat.skew_tableau as skew_tableau
        sage: t = SkewTableau([[None, 1, 3], [None, 2], [4]])
        sage: shape = t.shape()
        sage: word  = t.to_word()
        sage: skew_tableau.from_shape_and_word(shape, word)
        [[None, 1, 3], [None, 2], [4]]
    """
    st = [ [None]*row_length for row_length in shape[0] ]
    w_count = 0
    for i in reversed(range(len(shape[0]))):
        for j in range(shape[0][i]):
            if i >= len(shape[1]) or j >= shape[1][i]:
                st[i][j] = word[w_count]
                w_count += 1
    return SkewTableau(st)


# Deprecation of internal classes seems to be unnecessarily painful...
from sage.misc.superseded import deprecation

def SemistandardSkewTableaux_n(*args, **kargs):
    """
    EXAMPLES::

        sage: sage.combinat.skew_tableau.SemistandardSkewTableaux_n(3)
        doctest:1: DeprecationWarning: this class is deprecated. Use SemistandardSkewTableaux_size instead
        See http://trac.sagemath.org/9265 for details.
        Semistandard skew tableaux of size 3
    """
    deprecation(9265,'this class is deprecated. Use SemistandardSkewTableaux_size instead')
    return SemistandardSkewTableaux(*args, **kargs)

def SemistandardSkewTableaux_nmu(*args, **kargs):
    """
    EXAMPLES::

        sage: sage.combinat.skew_tableau.SemistandardSkewTableaux_nmu(3,[2,1])
        doctest:1: DeprecationWarning: this class is deprecated. Use SemistandardSkewTableaux_size_weight instead
        See http://trac.sagemath.org/9265 for details.
        Semistandard skew tableaux of size 3 and weight [2, 1]
    """
    deprecation(9265,'this class is deprecated. Use SemistandardSkewTableaux_size_weight instead')
    return SemistandardSkewTableaux(*args, **kargs)

def SemistandardSkewTableaux_p(*args, **kargs):
    """
    EXAMPLES::

        sage: sage.combinat.skew_tableau.SemistandardSkewTableaux_p([[2,1],[]])
        doctest:1: DeprecationWarning: this class is deprecated. Use SemistandardSkewTableaux_shape instead
        See http://trac.sagemath.org/9265 for details.
        Semistandard skew tableaux of shape [[2, 1], []]
    """
    deprecation(9265,'this class is deprecated. Use SemistandardSkewTableaux_shape instead')
    return SemistandardSkewTableaux_shape(*args, **kargs)

def SemistandardSkewTableaux_pmu(*args, **kargs):
    """
    EXAMPLES::

        sage: sage.combinat.skew_tableau.SemistandardSkewTableaux_pmu([[2,1],[]],[2,1])
        doctest:1: DeprecationWarning: this class is deprecated. Use SemistandardSkewTableaux_shape_weight instead
        See http://trac.sagemath.org/9265 for details.
        Semistandard skew tableaux of shape [[2, 1], []] and weight [2, 1]
    """
    deprecation(9265,'this class is deprecated. Use SemistandardSkewTableaux_shape_weight instead')
    return SemistandardSkewTableaux_shape_weight(*args, **kargs)

def StandardSkewTableaux_n(*args, **kargs):
    """
    EXAMPLES::

        sage: sage.combinat.skew_tableau.StandardSkewTableaux_n(2)
        doctest:1: DeprecationWarning: this class is deprecated. Use StandardSkewTableaux_size instead
        See http://trac.sagemath.org/9265 for details.
        Standard skew tableaux of size 2
    """
    deprecation(9265,'this class is deprecated. Use StandardSkewTableaux_size instead')
    return StandardSkewTableaux(*args, **kargs)

# October 2012: fixing outdated pickles which use the classes being deprecated
from sage.structure.sage_object import register_unpickle_override
register_unpickle_override('sage.combinat.skew_tableau', 'StandardSkewTableaux_n',  StandardSkewTableaux_size)
register_unpickle_override('sage.combinat.skew_tableau', 'SemistandardSkewTableaux_n',  SemistandardSkewTableaux_size)
register_unpickle_override('sage.combinat.skew_tableau', 'SemistandardSkewTableaux_nmu',  SemistandardSkewTableaux_size_weight)
register_unpickle_override('sage.combinat.skew_tableau', 'SemistandardSkewTableaux_p',  SemistandardSkewTableaux_shape)
register_unpickle_override('sage.combinat.skew_tableau', 'SemistandardSkewTableaux_pmu',  SemistandardSkewTableaux_shape_weight)
