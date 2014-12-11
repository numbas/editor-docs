.. _jme:

JME
===

JME expressions are used by students to enter answers to algebraic questions, and by question authors to define variables. JME syntax is similar to what you'd type on a calculator.

.. _variable-names:

Variable names
***************

Variable names are case-insensitive, so ``y`` represents the same thing as ``Y``. The first character of a variable name must be an alphabet letter; after that, any combination of letters and numbers is allowed, with any number of ``'`` on the end.

**Examples**: 
    * ``x``
    * ``var1``
    * ``row1val2``
    * ``y''``

``e``, ``i`` and ``pi`` are reserved names representing mathematical constants. They are rewritten by the interpreter to their respective numerical values before evaluation.

Names can be given annotations to change how they are displayed. The following annotations are built-in:

* ``verb`` – does nothing, but names like ``i``, ``pi`` and ``e`` are not interpreted as the famous mathematical constants.
* ``op`` – denote the name as the name of an operator — wraps the name in the LaTeX \operatorname command when displayed
* ``v`` or ``vector`` – denote the name as representing a vector — the name is displayed in boldface
* ``unit`` – denote the name as representing a unit vector — places a hat above the name when displayed
* ``dot`` – places a dot above the name when displayed, for example when representing a derivative
* ``m`` or ``matrix`` – denote the name as representing a matrix — displayed using a non-italic font

Any other annotation is taken to be a LaTeX command. For example, a name ``vec:x`` is rendered in LaTeX as ``\vec{x}``, which places an arrow above the name.

This screencast describes which variable names are valid, and gives some advice on how you should pick names:

.. raw:: html
    
    <div style="text-align: center;"><iframe src="http://player.vimeo.com/video/59577617" width="600" height="337" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

.. _jme-data-types:

Data types
**********

.. data:: number

    Numbers include integers, real numbers and complex numbers. There is only one data type for all numbers.

    ``i``, ``e``, ``infinity`` and ``pi`` are reserved keywords for the imaginary unit, the base of the natural logarithm, ∞ and π, respectively.

    **Examples**: ``0``, ``-1``, ``0.234``, ``i``, ``e``, ``pi``

.. data:: boolean

    Booleans represent either truth or falsity. The logical operations and, or and xor operate on and return booleans.

    **Examples**: ``true``, ``false``

.. data:: string

    Use strings to create non-mathematical text. Either ``'`` or ``"`` can be used to delimit strings.

    **Examples**: ``"hello there"``, ``'hello there'``

.. data:: list

    An ordered list of elements of any data type.

    **Examples**: ``[0,1,2,3]``, ``[a,b,c]``, ``[true,false,true]``

.. data:: range

    A range ``a..b#c`` represents (roughly) the set of numbers :math:`\{a+nc \: | \: 0 \leq n \leq \frac{b-a}{c} \}`. If the step size is zero, then the range is the continuous interval :math:`[a,b]`.

    **Examples**: ``1..3``, ``1..3#0.1``, ``1..3#0``

.. data:: vector

    The components of a vector must be numbers.

    When combining vectors of different dimensions, the smaller vector is padded with zeroes to make up the difference.

    **Examples**: ``vector(1,2)``, ``vector([1,2,3,4])``

.. data:: matrix

    Matrices are constructed from lists of numbers, representing the rows.

    When combining matrices of different dimensions, the smaller matrix is padded with zeroes to make up the difference.
    
    **Examples**: ``matrix([1,2,3],[4,5,6])``, ``matrix(row1,row2,row3)``

.. data:: html

    An HTML DOM node.

    **Examples**: ``html("<div>things</div>")``

Function reference
******************

Arithmetic
----------

.. function:: x+y

    Addition. Numbers, vectors, matrices, lists, or strings can be added together.
    ``list1+list2`` concatenates the two lists, while ``list+value`` returns a list with the right-hand-side value appended.

    **Examples**: 
        * ``1+2`` → ``3``
        * ``vector(1,2)+vector(3,4)`` → ``vector(4,6)``
        * ``matrix([1,2],[3,4])+matrix([5,6],[7,8])`` → ``matrix([6,8],[10,12])``
        * ``[1,2,3]+4`` → ``[1,2,3,4]``
        * ``[1,2,3]+[4,5,6]`` → ``[1,2,3,4,5,6]``
        * ``"hi "+"there"`` → ``"hi there"``

.. function:: x-y

    Subtraction. Defined for numbers, vectors and matrices.

    **Examples**: 
        * ``1-2`` → ``-1``
        * ``vector(3,2)-vector(1,4)`` → ``vector(2,-2)``
        * ``matrix([5,6],[3,4])-matrix([1,2],[7,8])`` → ``matrix([4,4],[-4,-4])``

.. function:: x*y

    Multiplication. Numbers, vectors and matrices can be multiplied together.

    **Examples**: 
        * ``1*2`` → ``2``
        * ``2*vector(1,2,3)`` → ``vector(2,4,6)``
        * ``matrix([1,2],[3,4])*2`` → ``matrix([2,4],[6,8])``
        * ``matrix([1,2],[3,4])*vector(1,2)`` → ``vector(5,11)``

.. function:: x/y

    Division. Only defined for numbers. 

    **Example**: ``3/4`` → ``0.75``.

.. function:: x^y

    Exponentiation. Only defined for numbers.

    **Examples**: 
        * ``3^2`` → ``9``
        * ``exp(3,2)`` → ``9``
        * ``e^(pi * i)`` → ``-1``

Number operations
-----------------

.. function:: abs(x)

    Absolute value, or modulus. Defined for numbers, strings, ranges, vectors and lists. In the case of a list, returns the number of elements. For a range, returns the difference between the upper and lower bounds.

    **Examples**: 
        * ``abs(-8)`` → ``8``
        * ``abs(3-4i)`` → ``5``
        * ``abs("Hello")`` → ``5``
        * ``abs([1,2,3])`` → ``3``
        * ``len([1,2,3])`` → ``3``
        * ``length(vector(3,4))`` → ``5``
        * ``abs(vector(3,4,12))`` → ``13``

.. function:: arg(z)

    Argument of a complex number.

    **Example**: ``arg(-1)`` → ``pi``

.. function:: re(z)

    Real part of a complex number.

    **Example**: ``re(1+2i)`` → ``1``

.. function:: im(z)

    Imaginary part of a complex number.

    **Example**: ``im(1+2i)`` → ``2``

.. function:: conj(z)

    Complex conjugate.

    **Example**: ``conj(1+i)`` → ``1-i``

.. function:: isint(x)

    Returns ``true`` if ``x`` is an integer.

    **Example**: ``isint(4.0)`` → ``true``

.. function:: sqrt(x)

    Square root of a number.

    **Examples**: 
        * ``sqrt(4)`` → ``2``
        * ``sqrt(-1)`` → ``i``

.. function:: root(x,n)

    ``n``:sup:`th` root of ``x``.

    **Example**: ``root(8,3)`` → ``2``.

.. function:: ln(x)

    Natural logarithm.

    **Example**: ``ln(e)`` → ``1``

.. function:: log(x)

    Logarithm with base 10.

    **Example**: ``log(100)`` → ``2``.

.. function:: degrees(x)

    Convert radians to degrees.

    **Examples**: ``degrees(pi/2)`` → ``90``

.. function:: radians(x)

    Convert degrees to radians.

    **Examples**: ``radians(180)`` → ``pi``

.. function:: sign(x)

    Sign of a number. Equivalent to :math:`\frac{x}{|x|}`, or 0 when ``x`` is 0.

    **Examples**: 
        * ``sign(3)`` → ``1``
        * ``sign(-3)`` → ``-1``

.. function:: max(a,b)

    Greatest of two numbers.

    **Example**: ``max(46,2)`` → ``46``

.. function:: min(a,b)

    Least of two numbers.

    **Example**: ``min(3,2)`` → ``2``

.. function:: precround(n,d)

    Round ``n`` to ``d`` decimal places.

    **Example**: ``precround(pi,5)`` → ``3.14159``

.. function:: siground(n,d)

    Round ``n`` to ``d`` significant figures.

    **Example**: ``siground(pi,3)`` → ``3.14``

.. function:: dpformat(n,d)

    Round ``n`` to ``d`` decimal places and return a string, padding with zeroes if necessary.

    **Example**: ``dpformat(1.2,4)`` → ``"1.2000"``

.. function:: sigformat(n,d)

    Round ``n`` to ``d`` significant figures and return a string, padding with zeroes if necessary.

    **Example**: ``sigformat(4,3)`` → ``4.00``

Trigonometry
------------

Trigonometric functions all work in radians, and have domain the complex numbers.

.. function:: sin(x)

.. function:: cos(x)

.. function:: tan(x)

.. function:: cosec(x)

.. function:: sec(x)

.. function:: cot(x)

.. function:: arcsin(x)

.. function:: arccos(x)

.. function:: arctan(x)

.. function:: sinh(x)

.. function:: cosh(x)

.. function:: tanh(x)

.. function:: cosech(x)

.. function:: sech(x)

.. function:: coth(x)

.. function:: arcsinh(x)

.. function:: arccosh(x)

.. function:: arctanh(x)

Number theory
-------------

.. function:: fact(x)

    Factorial. When ``x`` is not an integer, :math:`\Gamma(x+1)` is used instead.

    **Examples**: 
        * ``fact(3)`` → ``6``
        * ``3!`` → ``6``
        * ``fact(5.5)`` → ``287.885277815``

.. function:: factorise(n)

    Factorise ``n``. Returns the exponents of the prime factorisation of ``n`` as a list.

    **Examples**
        * ``factorise(18)`` → ``[1,2]``
        * ``factorise(70)`` → ``[1,0,1,1]``

.. function:: gamma(x)

    Gamma function.

    **Examples**: 
        * ``gamma(3)`` → ``2``
        * ``gamma(1+i)`` → ``0.4980156681 - 0.1549498283i``

.. function:: ceil(x)

    Round up to the nearest integer. When ``x`` is complex, each component is rounded separately.

    **Examples**: 
        * ``ceil(3.2)`` → ``4``
        * ``ceil(-1.3+5.4i)`` → ``-1+6i``

.. function:: floor(x)

    Round down to the nearest integer. When ``x`` is complex, each component is rounded separately.

    **Example**: ``floor(3.5)`` → ``3``

.. function:: trunc(x)

    If ``x`` is positive, round down to the nearest integer; if it is negative, round up to the nearest integer.

    **Example**: 
        * ``trunc(3.3)`` → ``3``
        * ``trunc(-3.3)`` → ``-3``

.. function:: fract(x)

    Fractional part of a number. Equivalent to ``x-trunc(x)``.

    **Example**: ``fract(4.3)`` → ``0.3``

.. function:: mod(a,b)

    Modulo; remainder after integral division, i.e. :math:`a \bmod b`.

    **Example**: ``mod(5,3)`` → ``2``

.. function:: perm(n,k)

    Count permutations, i.e. :math:`^n \kern-2pt P_r`.

    **Example**: ``perm(5,2)`` → ``60``

.. function:: comb(n,k)

    Count combinations, i.e. :math:`^n \kern-2pt C_r`.

    **Example**: ``comb(5,2)`` → ``10``.

.. function:: gcd(a,b)

    Greatest common divisor of integers ``a`` and ``b``. Can also write ``gcf(a,b)``.

    **Example**: ``gcd(12,16)`` → ``4``

.. function:: lcm(a,b)

    Lowest common multiple of integers ``a`` and ``b``. Can be used with any number of arguments; it returns the lowest common multiple of all the arguments.

    **Examples** 
        * ``lcm(8,12)`` → ``24``
        * ``lcm(8,12,5)`` → ``120``

.. function:: x|y

    ``x`` divides ``y``.

    **Example**: ``4|8`` → ``true``

Vector arithmetic
-----------------

.. function:: vector(a1,a2,...,aN)

    Create a vector with given components. Alternately, you can create a vector from a single list of numbers.

    **Examples**:
        * ``vector(1,2,3)``
        * ``vector([1,2,3])``

.. function:: matrix(row1,row2,...,rowN)

    Create a matrix with given rows, which should be lists of numbers. Or, you can pass in a single list of lists of numbers.

    **Examples**: 
        * ``matrix([1,2],[3,4])``
        * ``matrix([[1,2],[3,4]])``

.. function:: rowvector(a1,a2,...,aN)

    Create a row vector (:math:`1 \times n` matrix) with the given components. Alternately, you can create a row vector from a single list of numbers.

    **Examples**: 
        * ``rowvector(1,2)`` → ``matrix([1,2])``
        * ``rowvector([1,2])`` → ``matrix([1,2])``

.. function:: dot(x,y)

    Dot (scalar) product. Inputs can be vectors or column matrices.

    **Examples**: ``dot(vector(1,2,3),vector(4,5,6))``, ``dot(matrix([1],[2]), matrix([3],[4])``.

.. function:: cross(x,y)

    Cross product. Inputs can be vectors or column matrices.

    **Examples**: ``cross(vector(1,2,3),vector(4,5,6))``, ``cross(matrix([1],[2]), matrix([3],[4])``.

.. function:: det(x)

    Determinant of a matrix. Only defined for up to 3x3 matrices.

    **Examples**: ``det(matrix([1,2],[3,4]))``, ``det(matrix([1,2,3],[4,5,6],[7,8,9]))``.

.. function:: transpose(x)
    
    Matrix transpose. Can also take a vector, in which case it returns a single-row matrix.

    **Examples**: ``transpose(matrix([1,2],[3,4]))``, ``transpose(vector(1,2,3))``.

.. function:: id(n)

    Identity matrix with :math:`n` rows and columns.

    **Example**: ``id(3)``.

Strings
------------------

.. function:: latex(x)

    Mark string ``x`` as containing raw LaTeX, so when it's included in a mathmode environment it doesn't get wrapped in a ``\textrm`` environment.

    **Example**: ``latex('\frac{1}{2}')``.

.. function:: capitalise(x)

    Capitalise the first letter of a string.

    **Example**: ``capitalise('hello there')``.

.. function:: pluralise(n,singular,plural)

    Return ``singular`` if ``n`` is 1, otherwise return ``plural``.

    **Example**: ``pluralise(num_things,"thing","things")``

.. function:: upper(x)

    Convert string to upper-case.

    **Example**: ``upper('Hello there')``.

.. function:: lower(x)

    Convert string to lower-case.

    **Example**: ``lower('CLAUS, Santa')``.

.. function:: join(strings, delimiter)

    Join a list of strings with the given delimiter.

    **Example**: ``join(['a','b','c'],',')`` → ``'a,b,c'``

Logic
-----

.. function:: x<y

    Returns ``true`` if ``x`` is less than ``y``. Defined only for numbers.

    **Examples**: ``4<5``.

.. function:: x>y

    Returns ``true`` if ``x`` is greater than ``y``. Defined only for numbers.

    **Examples**: ``5>4``.

.. function:: x<=y

    Returns ``true`` if ``x`` is less than or equal to ``y``. Defined only for numbers.

    **Examples**: ``4<=4``.

.. function:: x>=y

    Returns ``true`` if ``x`` is greater than or equal to ``y``. Defined only for numbers.

    **Examples**: ``4>=4``.

.. function:: x<>y

    Returns ``true`` if ``x`` is not equal to ``y``. Defined for any data type. Returns ``true`` if ``x`` and ``y`` are not of the same data type.

    **Examples**: ``'this string' <> 'that string'``, ``1<>2``, ``'1' <> 1``.

.. function:: x=y

    Returns ``true`` if ``x`` is equal to ``y``. Defined for any data type. Returns ``false`` if ``x`` and ``y`` are not of the same data type.

    **Examples**: ``vector(1,2)=vector(1,2,0)``, ``4.0=4``.

.. function:: x and y

    Logical AND.

    **Examples**: ``true and true``, ``true && true``, ``true & true``.

.. function:: not x

    Logical NOT.

    **Examples**: ``not true``, ``!true``.

.. function:: x or y

    Logical OR.

    **Examples**: ``true or false``, ``true || false``.

.. function:: x xor y

    Logical XOR.

    **Examples**: ``true XOR false``.

Ranges
------

.. function:: a..b

    Define a range. Includes all integers between and including ``a`` and ``b``.

    **Examples**: ``1..5``, ``-6..6``.

.. function:: a..b#s

    Set the step size for a range. Default is 1. When ``s`` is 0, the range includes all real numbers between the limits.

    **Examples**: ``0..1 # 0.1``, ``2..10 # 2``, ``0..1#0``.

.. function:: a except b

    Exclude a number, range, or list of items from a list or range.

    **Examples**: ``-9..9 except 0``, ``-9..9 except [-1,1]``. ``3..8 except 4..6``, ``[1,2,3,4,5] except [2,3]``.

Lists
-----

.. function:: x[n]

    Get the ``n``:sup:`th` element of list, vector or matrix ``x``. For matrices, the ``n``:sup:`th` row is returned.

    **Example**: 
        * ``[0,1,2,3][1]`` → ``1``
        * ``vector(0,1,2)[2]`` → ``2``
        * ``matrix([0,1,2],[3,4,5],[6,7,8])[0]`` → ``matrix([0,1,2])``

.. function:: x[a..b]

    Slice list ``x`` - return elements with indices in the given range.

    **Example**: ``[0,1,2,3,4,5][1..3]`` → ``[1,2,3]``

.. function:: repeat(expression,n)

    Evaluate ``expression`` ``n`` times, and return the results in a list.

    **Example**: ``repeat(random(1..4),5)`` → ``[2, 4, 1, 3, 4]``

.. function:: map(expression,name,d)

    Evaluate ``expression`` for each item in list or range ``d``, replacing variable ``name`` with the element from ``d`` each time.

    .. note::
        Do not use ``i`` or ``e`` as the variable name to map over - they're already defined as mathematical constants!

    **Examples**: 
        * ``map(x+1,x,1..3)`` → ``[2,3,4]``
        * ``map(capitalise(s),s,["jim","bob"])`` → ``["Jim","Bob"]``

.. function:: sort(x)

    Sort list ``x``.

    **Example**: ``sort([4,2,1,3])`` → ``[1,2,3,4]``

.. function:: distinct(x)

    Return a copy of the list ``x`` with duplicates removed.

    **Example**: ``distinct([1,2,3,1,4,3])`` → ``[1,2,3,4]``

.. function:: list(x)

    Convert vector or matrix ``x`` to a list of components or rows, respectively.

    **Examples**: 
        * ``list(vector(1,2))`` → ``[1,2]``
        * ``list(matrix([1,2],[3,4]))`` → ``[[1,2], [3,4]]``

.. function:: satisfy(names,definitions,conditions,maxRuns)

    Each variable name in ``names`` should have a corresponding definition expression in ``definitions``. ``conditions`` is a list of expressions which you want to evaluate to ``true``. The definitions will be evaluated repeatedly until all the conditions are satisfied, or the number of attempts is greater than ``maxRuns``. If ``maxRuns`` isn't given, it defaults to 100 attempts.

    **Example**: ``satisfy([a,b,c],[random(1..10),random(1..10),random(1..10)],[b^2-4*a*c>0])``

.. function:: sum(numbers)

    Add up a list of numbers

    **Example**: ``sum([1,2,3])`` → ``6``

Randomisation
-------------

.. function:: random(x)

    Pick uniformly at random from a range, list, or from the given arguments.

    **Examples**: 
        * ``random(1..5)``
        * ``random([1,2,4])``
        * ``random(1,2,3)``

.. function:: deal(n)

    Get a random shuffling of the integers :math:`[0 \dots n-1]`

    **Example**: ``deal(3)`` → ``[2,0,1]``

.. function:: shuffle(x)

    Random shuffling of list ``x``.

    **Example**: ``shuffle(["a","b","c"])`` → ``["c","b","a"]``

Control flow
------------

.. function:: award(a,b)

    Return ``a`` if ``b`` is ``true``, else return ``0``.

    **Example**: ``award(5,true)`` → ``5``

.. function:: if(p,a,b)

    If ``p`` is ``true``, return ``a``, else return ``b``. Only the returned value is evaluated.

    **Example**: ``if(false,1,0)`` → ``0``

.. function:: switch(p1,a1,p2,a2, ..., pn,an,d)

    Select cases. Alternating boolean expressions with values to return, with the final argument representing the default case. Only the returned value is evaluated.

    **Examples**: 
        * ``switch(true,1,false,0,3)`` → ``1``
        * ``switch(false,1,true,0,3)`` → ``0``
        * ``switch(false,1,false,0,3)`` → ``3``

HTML
----

.. function:: html(x)

    Parse string ``x`` as HTML.

    **Examples**: ``html('<div>Text!</div>')``.

.. function:: table(data,headers)

    Create an HTML with cell contents defined by ``data``, which should be a list of lists of data, and column headers defined by the list of strings ``headers``.

    **Example**: ``table([[0,1],[1,0]], ["Column A","Column B"])``

.. function:: image(url)

    Create an HTML `img` element loading the image from the given URL. Images uploaded through the resources tab are stored in the relative URL `resources/images/<filename>.png`, where `<filename>` is the name of the original file.

    **Examples**: 
        * ``image('resources/images/picture.png')``
        * ``image(chosenimage)``
        * `Question using randomly chosen images <https://numbas.mathcentre.ac.uk/question/1132/using-a-randomly-chosen-image/>`_.
