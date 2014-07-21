Pattern-matching mathematical expressions
=========================================

.. ref:: pattern-matching

.. warning::

    The pattern-matching algorithm is new and experimental. It opens up many new possibilities for providing adaptive feedback and manipulating mathematical expressions in general, but the interface is currently quite cumbersome. This documentation will be expanded as the system is used more.

Numbas includes a sophisticated pattern-matching algorithm for mathematical expressions. It's mainly used by the ``\simplify`` command, but can also be used in, for example, custom marking scripts to answer more nuanced questions about the form of the student's answer.

The pattern-matcher should be considered to work similarly to how a regular expression algorithm, except it operates on algebraic syntax trees instead of text strings. The algorithm will either return ``false``, when the expression doesn't match the pattern, or ``true``, and a dictionary of named matching groups, which are sub-trees of the input expression.

Using the pattern matcher
-------------------------

The function `Numbas.jme.display.matchExpression(pattern,expression) <http://numbas.github.io/Numbas/Numbas.jme.display.html#matchExpression>`_ matches a JME expression against a pattern. The pattern is also written in JME syntax, but there are extra operators available to allow extra control what does or doesn't match.

The parameters of a commutative operation in the pattern (i.e. addition, multiplication, or equality) can match in any order. The algorithm matches greedily, reading from left to right in both the pattern to match and the input expression.

Pattern-matching should only be used for assigning marks when the *form* of the student's answer is what's being assessed, for example when the student is asked to factorise a quadratic or reduce a fraction to lowest terms. For answers which are the result of a calculation, you should use the normal numerical marking algorithms because pattern-matching can be too restrictive (or, if you're not careful, too accepting!) In such cases, you could use pattern-matching to provide feedback about possible errors the student made, when their answer is marked wrong by the numerical algorithm.

Pattern-matching syntax
-----------------------

.. object:: ?

    Match anything.

.. object:: ??

    Match anything or nothing.

.. object:: expr;g

    Capture ``expr`` in the group named ``g``.

.. object:: m_any(expr1,expr2,...)

    Match any of the expressions ``exprN``.

.. object:: m_all(expr)

    Capture all terms (in an addition, multiplication, or other commutative operation) matching ``expr``.

.. object:: m_pm(expr)

    Capture ``expr`` or ``-(expr)``, i.e. plus or minus the given expression.

.. object:: m_not(expr)

    Match anything *except* ``expr``.

.. object:: m_uses(name1,name2,...)

    Match any expression which uses the given variable names.

.. object:: m_commute(expr)

    Match the terms in ``expr`` in any order, following the laws of commutativity. (This is only required if you are using ``matchExpression`` with the ``doCommute`` flag set to ``false``, and you only want to use commutativity in certain places)

.. object:: m_nothing

    Match nothing. Useful as an empty term to act as the right-hand side of an addition, where you want to capture all terms in the left-hand side.

To help with learning the new syntax, there is an online tool to test expressions against patterns at http://www.staff.ncl.ac.uk/christian.perfect/patternmatching/matching.html

Examples
--------

Get all $x$ terms in a polynomial::

    m_all(m_pm(m_all(??)*m_any(x,x^?)));xs+m_all(??);rest

Get the coefficient and degree of an $x$ term::

    m_pm(m_all(??);coefficient*m_any(x,x^?;degree))

Get both sides of an equation::

    ?;left=?;right

Check $x$ terms are collected on one side of an equation::

    m_uses(x);xside = m_not(m_uses(x));otherside

Check that a quadratic is factorised::

    (m_pm(??*x);a+?;b)*(m_pm(??*x);c+?;d)

Capture multiple powers of $x$ and $y$::

    m_all( m_any( ??x, ??y, ??x^??, ??y^??, m_any(x,x^??)*m_any(y,y^??)*?? ) );terms + m_all(??;rest)
