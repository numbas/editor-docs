.. _simplification-rules:

Displaying maths
====================

Maths is displayed using LaTeX. A good place to learn LaTeX is the `Art of Problem Solving LaTeX Guide <http://www.artofproblemsolving.com/Wiki/index.php/LaTeX:Commands>`_.

Write in-line maths between dollar signs, like so::

    $e^{\pi i} + 1 = 0$

Which produces: :math:`e^{\pi i} + 1 = 0`.

Larger formulae and equations should be written in display mode, like so::

    \[ \int_0^1 e^{-x^2} dx \]

Which produces:

.. math::
    
    \int_0^1 e^{-x^2} dx

LaTeX is purely a typesetting language and is ill-suited for representing *meaning* in addition to *layout*. For this reason, dynamic or randomised maths expressions must be written in JME syntax and converted to LaTeX. Numbas provides two new LaTeX commands to do this for you.

To *substitute* the result of an expression into a LaTeX expression, use the ``\var`` command. Its parameter is a JME expression, which is evaluated and then converted to LaTeX.

For example::

    \[ \var{2^3} \]

produces::

    \[ 8 \]

and if a variable called x has been defined to have the value 3::

    \[ 2^{\var{x}} \]

produces::

    \[ 2^{3} \]

This simple substitution doesn't always produce attractive results, for example when substituted variables might have negative values. If :math:`y=-4`::

\[ \var{x} + \var{y} \]

produces::

    \[ 3 + -4 \]

To deal with this, and other more complicated substitutions, there is the ``\simplify`` command.

The main parameter of the ``\simplify`` command is a JME expression. It is not evaluated - it is converted into LaTeX as it stands. For example::

    \[ \simplify{ x + (-1/y) } \]

produces::

    \[ x - \frac{1}{y} \]

Variables can be substituted in by enclosing them in curly braces. For example::

    \[ \simplify{ {x} + {y} } \]

produces::

    \[ 3 - 4 \]

The ``\simplify`` command automatically rearranges expressions, according to a set of simplification rules, to make them look more natural. Sometimes you might not want this to happen, for example while writing out the steps in a worked solution.

The set of rules to be used is defined in a list enclosed in square brackets before the main argument of the ``\simplify`` command. You can control the ``\simplify`` command's behaviour by switching rules on or off.

For example, in::

    \[ \simplify{ 1*x } \]

I have not given a list of rules to use, so they are all switched on. The ``unitFactor`` rule cancels the redundant factor of 1 to produce::

    \[ x \]

while in::

    \[ \simplify[!unitFactor]{ 1*x } \]

I have turned off the unitFactor rule, leaving the expression as it was::

    \[ 1 x \]

When a list of rules is given, the list is processed from left to right. Initially, no rules are switched on. When a rule's name is read, that rule is switched on, or if it has an exclamation mark in front of it, that rule is switched off.

Sets of rules can be given names in the exam's :ref:`rulesets` section, so they can be turned on or off in one go.


Simplification rules
********************

The ``\simplify`` command takes an optional list of names of rules to use, separated by commas. Lists of simplification rule names are read from left to right, and rules are added or removed from the set in use as their names are read. To include a rule, use its name, e.g. ``unitfactor``. To exclude a rule, put an exclamation mark in front of its name, e.g. ``!unitfactor``.

Rule names are not case-sensitive: any mix of lower-case or upper-case works. 

To turn all built-in rules on, use the name ``all``. To turn all built-in rules off, use ``!all``.

.. glossary::

    basic
        These rules are always turned on, even if you give an empty list of rules. They must be actively turned off, by including ``!basic`` in the list of rules.

        * ``+x`` → ``x`` (get rid of unary plus)
        * ``x+(-y)`` → ``x-y`` (plus minus = minus)
        * ``x-(-y)`` → ``x+y`` (minus minus = plus)
        * ``-(-x)`` → ``x`` (unary minus minus = plus)
        * ``-x`` → ``eval(-x)`` (if unary minus on a complex number with negative real part, rewrite as a complex number with positive real part)
        * ``x+y`` → ``eval(x+y)`` (always collect imaginary parts together into one number)
        * ``-x+y`` → ``-eval(x-y)`` (similarly, for negative numbers)
        * ``(-x)/y`` → ``-(x/y)`` (take negation to left of fraction)
        * ``x/(-y)`` → ``-(x/y)``
        * ``(-x)*y`` → ``-(x*y)`` (take negation to left of multiplication)
        * ``x*(-y)`` → ``-(x*y)``
        * ``x+(y+z)`` → ``(x+y)+z`` (make sure sums calculated left-to-right)
        * ``x-(y+z)`` → ``(x-y)-z``
        * ``x+(y-z) ``(x+y)-z'``
        * ``x-(y-z)`` > ``(x-y)+z``
        * ``(x*y)*z`` → ``x*(y*z)`` (make sure multiplications go right-to-left)
        * ``n*i`` → ``eval(n*i)`` (always collect multiplication by :math:`i`)
        * ``i*n`` → ``eval(n*i)``

    unitFactor
        Cancel products of 1

        * ``1*x`` → ``x``
        * ``x*1`` → ``x``

    unitPower
        Cancel exponents of 1

        * ``x^1`` → ``x``

    unitDenominator
        Cancel fractions with denominator 1

        * ``x/1`` → ``x``

    zeroFactor
        Cancel products of zero to zero

        * ``x*0`` → ``0``
        * ``0*x`` → ``0``
        * ``0/x`` → ``0``

    zeroTerm
        Omit zero terms

        * ``0+x`` → ``x``
        * ``x+0`` → ``x``
        * ``x-0`` → ``x``
        * ``0-x`` → ``-x``

    zeroPower
        Cancel exponents of 0

        * ``x^0`` → ``1``

    noLeadingMinus
        Rearrange expressions so they don't start with a unary minus

        * ``-x+y`` → ``y-x``

    collectNumbers
        Collect together numerical (as opposed to variable) products and sums. The rules below are only applied if ``n`` and ``m`` are numbers.
    
        * ``-x-y`` → ``-(x+y)`` (collect minuses)
        * ``n+m`` → ``eval(n+m)`` (add numbers)
        * ``n-m`` → ``eval(n-m)`` (subtract numbers)
        * ``n+x`` → ``x+n`` (numbers go to the end of expressions)
        * ``(x+n)+m`` → ``x+eval(n+m)`` (collect number sums)
        * ``(x-n)+m`` → ``x+eval(m-n)``
        * ``(x+n)-m`` → ``x+eval(n-m)``
        * ``(x-n)-m)`` → ``x-eval(n+m)``
        * ``(x+n)+y`` → ``(x+y)+n`` (numbers go to the end of expressions)
        * ``(x+n)-y`` → ``(x-y)+n``
        * ``(x-n)+y`` → ``(x+y)-n``
        * ``(x-n)-y`` → ``(x-y)-n)``
        * ``n*m`` → ``eval(n*m)`` (multiply numbers)
        * ``x*n`` → ``n*x`` (numbers go to left hand side of multiplication, unless :math:`n=i`)
        * ``m*(n*x)`` → ``eval(n*m)*x``

    simplifyFractions
        Cancel fractions to lowest form. The rules below are only applied if ``n`` and ``m`` are numbers and :math:`gcd(n,m) \gt 1`.

        * ``n/m`` → ``eval(n/gcd(n,m))/eval(m/gcd(n,m))`` (cancel simple fractions)
        * ``(n*x)/m`` → ``(eval(n/gcd(n,m))*x)/eval(m/gcd(n,m))`` (cancel algebraic fractions)
        * ``n/(m*x)`` → ``eval(n/gcd(n,m))/(eval(m/gcd(n,m))*x)``
        * ``(n*x)/(m*y)`` → ``(eval(n/gcd(n,m))*x)/(eval(m/gcd(n,m))*y)``

    zeroBase
        Cancel any power of zero

        * ``0^x`` → ``0``

    constantsFirst
        Numbers go to the left of multiplications

        * ``x*n`` → ``n*x``
        * ``x*(n*y)`` → ``n*(x*y)``

    sqrtProduct
        Collect products of square roots

        * ``sqrt(x)*sqrt(y)`` → ``sqrt(x*y)``

    sqrtDivision
        Collect fractions of square roots

        * ``sqrt(x)/sqrt(y)`` → ``sqrt(x/y)``

    sqrtSquare
        Cancel square roots of squares, and squares of square roots

        * ``sqrt(x^2)`` → ``x``
        * ``sqrt(x)^2`` → ``x``
        * ``sqrt(n)`` → ``eval(sqrt(n))``   (if ``n`` is a square number)

    trig
        Simplify some trigonometric identities

        * ``sin(n)`` → ``eval(sin(n))`` (if ``n`` is a multiple of :math:`\frac{\pi}{2}`)
        * ``cos(n)`` → ``eval(cos(n))`` (if ``n`` is a multiple of :math:`\frac{\pi}{2}`)
        * ``tan(n)`` → ``0`` (if ``n`` is a multiple of :math:`\pi`)
        * ``cosh(0)`` → ``1``
        * ``sinh(0)`` → ``0``
        * ``tanh(0)`` → ``0``

    otherNumbers
        Evaluate powers of numbers. This rule is only applied if ``n`` and ``m`` are numbers.

        * ``n^m`` → ``eval(n^m)``

    fractionNumbers
        This rule doesn't rewrite expressions, but tells the maths renderer that you'd like non-integer numbers to be displayed as fractions (e.g. :math:`\frac{1}{2}`) instead of decimals (e.g. :math:`0.5`).

    rowVector
        This rule doesn't rewrite expressions, but tells the maths renderer that you'd like vectors to be rendered as rows instead of columns.
