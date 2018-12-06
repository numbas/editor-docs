.. _pattern-matching:

Pattern-matching mathematical expressions
=========================================

Numbas includes a sophisticated pattern-matching algorithm for mathematical expressions. 
Pattern-matching is used to power the :ref:`simplification rules <simplification-rules>`, as well as to establish the *form* of mathematical expressions entered by the student.

The pattern-matcher should be considered to work similarly to a `regular expression algorithm <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions>`_, except it operates on algebraic syntax trees instead of text strings. 
The algorithm decides whether an input expression matches a given pattern, and also identifies `named matching groups`, which are sub-expressions of the input expression.


Pattern-matching syntax
-----------------------

Patterns are written in JME syntax, but there are extra operators available to specify what does or doesn't match.

The pattern-matching algorithm uses a few techniques to match different kinds of expression.

**Data elements** such as numbers, strings, booleans are matched by comparison: a pattern consisting of a single data element matches only that exact element.

A pattern consisting of a **function application** function application ``f(arguments...)`` matches any expression consisting of an application of exactly that function, and whose arguments, considered as a sequence, match the sequence of patterns ``arguments``.
There are some special functions which match differently.
If the same name is captured by more than one argument, then all the groups captured under that name are gathered into a list.

A pattern consisting of a sequence of terms joined by a binary **operator**, or a single term with a unary operator applied, is considered as a sequence. 
If a way of matching up the terms in the input expression with the terms in the pattern can be found, considering quantifiers and the properties of commutativity and associativity, then the expression matches the pattern.
If the same name is captured by more than one argument, then all the groups captured under that name are gathered into a sequence joined by the operator being matched.

A pattern consisting of a **list** matches any expression consisting of a single list, whose elements match the elements of the list in the pattern.
Quantifiers allow you to write a pattern which matches lists with different numbers of terms.

Special names
#############

.. jme:variable:: ?

    Matches anything.

.. jme:variable:: $n

    Matches a number.
    You can use the following annotations to restrict the kinds of numbers that are matched:

    * ``real`` - has no imaginary part.
    * ``complex`` - has a non-zero imaginary part.
    * ``imaginary`` - has a non-zero imaginary part and zero real part.
    * ``positive`` - real and strictly greater than 0.
    * ``nonnegative`` - real and greater than or equal to 0.
    * ``negative`` - real and less than 0.
    * ``integer`` - an integer.
    * ``decimal`` - written with at least one digit after the decimal place, or any real number with a fractional part.
    * ``rational`` - an integer, or the division of one integer by another. This doesn't match a single token - it's equivalent to the pattern ``integer:$n / integer:n`?``.

.. jme:variable:: $v

    Matches any variable name.

.. jme:variable:: $z

    Match nothing.
    Use this as the right-hand side of a ``+`` or ``*`` operation to force the pattern-matcher to match a sum or product, respectively, when the pattern would otherwise only contain one term, due to use of a quantifier.

Arithmetic Operators
####################

.. jme:function:: `+- X

    Match either ``X`` or ``-X``

.. jme:function:: `*/ X

    Match either ``X`` or ``1/X``

Combining patterns
##################

.. jme:function:: A `| B

    Match either ``A`` or ``B``.

.. jme:function:: A `& B

    The expression must match both ``A`` and ``B``.

.. jme:function:: `! X

    Match anything *except* ``X``.

.. jme:function:: X `where C

    The expression must match ``X``, and then the condition ``C`` is evaluated, with any names corresponding to groups captured in ``X`` substituted in.
    If the condition ``C`` evaluates to ``true``, the expression matches this pattern.

.. jme:function:: macros `@ X

    ``macros`` is a dictionary of patterns.
    The macros are substituted into ``X`` to produce a new pattern, which the expression must match.

Quantifiers
###########

Quantifiers are used to capture terms that may appear a variable number of times in a sequence.

.. jme:function:: X `?

    Either one occurrence of ``X`` or none.

.. jme:function:: X `: Y

    If the expression matches ``X``, match that, otherwise match as the default value ``Y``.

    In a sequence, this acts the same as the `` `?`` quantifier, additionally capturing the default value ``Y`` if ``X`` does not appear in the sequence.

.. jme:function:: X `*

    Any number of occurrences of ``X``, or none.

.. jme:function:: X `+

    At least one occurrence of ``X``.

Capturing named groups
######################

The *capturing operator* ``;`` captures attaches to a part of a pattern, and captures the part of the input expression matching that pattern under the given name.

.. jme:function:: X;g

    Capture the input expression in the group named ``g`` if it matches the pattern ``X``.

.. jme:function:: X;g:v

    Match ``X``, and capture the value ``v`` in the group named ``g``.

    You can use this to provide a default value for a value that's missing or implied, for example a coefficient of :math:`-1` in :math:`-x`.

.. jme:function:: X;=g

    Match ``X`` only if it's identical to every other occurrence captured under the name ``g``.

Matching modes
##############

The following functions change the way the matcher works.

.. glossary::

    Allow other terms
        
        When matching an associative operation, allow the presence of terms which don't match the pattern, as long as there are other terms which do satisfy the pattern.
        This allows you to write patterns which pick out particular parts of sums and products, for example, while ignoring the rest.
        This is equivalent to adding something like `` + ?`*`` to the end of every sum, and likewise for other associative operations.

    Use commutativity

        When matching an associative operation, allow the terms to appear in any order.
        A sequence matches if an ordering of the terms which satisfies the pattern can be found.

        For non-symmetric operators with converses, suchs as :math:`\lt` and :math:`\leq`, also match the converse relation, reversing the order of the operands.

    Use associativity

        For an associative operator :math:`\circ`, sequences of terms such as :math:`a \circ b \circ c` will be considered together.

        If this mode is not enabled, terms are not gathered into sequences before trying to match, so :math:`(a \circ b) \circ c` is not considered to be the same as :math:`a \circ (b \circ c)`.

    Gather as a list

        For an associative operator, when the same name is captured by multiple terms, the resulting captured group for that name is a list whose elements are the captured subexpressions from each term.

        If this mode is not enabled, the subexpressions from each term are joined together by the associative operator.
        This doesn't always make sense, particularly if the group captures only portions of each term.

    Strict inverse

        If this mode is not enabled, then :math:``a-b`` is matched as if it's :math:``a+(-b)``, and :math:`a/b` is matched as if it's :math:``a*(1/b)``.
        This makes matching sums of terms that may have negative coefficients easier.

        If this mode is enabled, then the behaviour described above is not used.

.. jme:function:: m_exactly(X)

    Turn off :term:`allow other terms` mode when matching ``X``.

.. jme:function:: m_commutative(X)

    Turn on :term:`use commutativity` mode when matching ``X``.

.. jme:function:: m_noncommutative(X)

    Turn off :term:`use commutativity` mode when matching ``X``.

.. jme:function:: m_associative(X)

    Turn on :term:`use associativity` mode when matching ``X``.

.. jme:function:: m_nonassociative(X)

    Turn off :term:`use associativity` mode when matching ``X``.

.. jme:function:: m_strictinverse(X)

    Turn on :term:`strict inverse` mode when matching ``X``.

.. jme:function:: m_gather(X)

    Turn on :term:`gather as a list` mode when matching ``X``.

.. jme:function:: m_nogather(X)

    Turn off :term:`gather as a list` mode when matching ``X``.

Special conditions
##################

.. jme:function:: m_type(type)

    Match any item with the given :ref:`data type <jme-data-types>`.

.. jme:function:: m_func(name,arguments)

    Match a function whose name, as a string, matches the given pattern, and whose arguments, considered as a :data:`list`, match the given pattern.

.. jme:function:: m_op(name,operands)

    Match a binary or unary operator whose name, as a string, matches the given pattern, and whose operands, considered as a :data:`list`, match the given pattern.

.. jme:function:: m_numeric(X)

    Match if a numerical comparison of ``X`` and the expression being considered says they're equivalent.

    Random values are chosen for the free variables, and substituted into both ``X`` and the input expression.
    If both expressions produce the same result, then the input expression matches this pattern.

.. jme:function:: m_anywhere(X)

    Match if a sub-expression matching the pattern ``X`` can be found anywhere inside the input expression.


Examples
--------

Get all :math:`x` terms in a polynomial::

    m_all(m_pm(m_all(??)*m_any(x,x^?)));xs+m_all(??);rest

Get the coefficient and degree of an :math:`x` term::

    m_pm(m_all(??);coefficient*m_any(x,x^?;degree))

Get both sides of an equation::

    ?;left=?;right

Check :math:`x` terms are collected on one side of an equation::

    m_uses(x);xside = m_not(m_uses(x));otherside

Check that a quadratic is factorised::

    (m_pm(??*x);a+?;b)*(m_pm(??*x);c+?;d)

Capture multiple powers of :math:`x` and :math:`y`::

    m_all( m_any( ??x, ??y, ??x^??, ??y^??, m_any(x,x^??)*m_any(y,y^??)*?? ) );terms + m_all(??;rest)
