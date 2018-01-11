.. _mathematical-expression:

Mathematical expression
^^^^^^^^^^^^^^^^^^^^^^^

Mathematical expression parts require the student to enter an algebraic expression, using :ref:`JME <jme>` syntax.

These parts are marked by picking a sample of points uniformly from a given range for the free variables in the expression, and evaluating both the student's answer and the correct answer on those points.
If the two expressions agree on enough inputs, then they are considered to be equivalent and the student's answer is marked as correct.

For questions where the student is asked to rearrange an expression, clearly just evaluating both answers won't detect the difference - you want to look at the *form* of the student's answer, as well as the values it produces.
The :ref:`string restrictions <string-restrictions>` offer a somewhat blunt method of restricting the form of the student's answer.
You can do more sophisticated testing with a :ref:`custom marking algorithm <marking-algorithm>` and :ref:`pattern-matching <pattern-matching>` on the student's answer.

.. topic:: Marking

    .. glossary::
        Correct answer
            The expected answer to the part. 
            Question variables (or, more broadly, JME expressions which should be evaluated to a single value when the question is generated), can be included by enclosing them in curly braces.

        Show preview of student's answer?
            If ticked, a rendering of the student's answer in mathematical notation is displayed beeside the input box. 
            You should leave this on unless you expect the answer to be veery simple and need the space - the feedback about how their answer is interpreted is very useful to students.

        Answer simplification rules
            :ref:`Simplification rules <simplification-rules>` to apply to the correct answer, if it is displayed to the student (for example, after clicking the :guilabel:`Reveal answers` button). 
            This shouldn't affect marking.
            
            If this field is empty,  the following rules are applied: ``basic``, ``unitFactor``, ``unitPower``, ``unitDenominator``, ``zeroFactor``, ``zeroTerm``, ``zeroPower``, ``collectNumbers``, ``zeroBase``, ``constantsFirst``, ``sqrtProduct``, ``sqrtDivision``, ``sqrtSquare``, ``otherNumbers``.


.. _string-restrictions:

.. topic:: String restrictions

    Before length restrictions are applied, surplus brackets and whitespace are removed, and spaces are inserted between some operations, to minimise the possibility of the length restrictions being triggered for the wrong reasons.

    .. glossary::

        Warn if student uses an unexpected variable name?
            If this is ticked, all variable names used in the student's are checked against the list you provide. 
            The first variable name which is not in the list will trigger a warning. 
            You can use this option to prevent students incorrectly entering answers such as ``xy``, which is interpreted as a single variable, when they mean ``x*y``, the product of two variables.

        Expected variable names
            Variable names in this list will not prompt the "unexpected variable name" warning when the student uses them. 

        Minimum length restriction
            If the student's answer contains fewer than this many characters, the penalty is applied. 
            A value of zero means no restriction is applied. 
            See the comment above on how the length is calculated.

        Maximum length restriction
            If the student's answer contains more than this many characters, the penalty is applied. 
            A value of zero means no restriction is applied.
            The student's answer is tidied up slightly so that things like extra or missing space characters don't affect the calculated length.
            All spaces are removed, and then spaces are inserted between binary operations.
            For example, the answer ``1+x`` (three characters) is marked as ``1 + x`` (five characters). 

        Required strings
            If the student's answer doesn't contain all of these strings, the penalty is applied.

        Forbidden strings
            If the student's answer contains any of these strings, the penalty is applied.

.. topic:: Accuracy

    These settings define the range of points over which the student's answer will be compared with the correct answer, and the method used to compare them.

    .. glossary::
        Checking type
            The rule to use to compare the student's answer with the correct answer.
            In the lines below, :math:`x` represents the value of the student's answer at a particular point and :math:`y` represents the value of the correct answer, while :math:`\delta` is the value of the checking accuracy property.

            * Absolute difference.
              Fail if :math:`\left| x-y \right| > \delta`.
            * Relative difference.
              Fail if :math:`\left| \frac{x}{y} - 1 \right| > \delta`.
            * Decimal points.
              :math:`x` and :math:`y` are rounded to :math:`\delta` decimal places, and the test fails if the rounded values are unequal.
            * Significant figures.
              :math:`x` and :math:`y` are rounded to :math:`\delta` significant figures, and the test fails if the rounded values are unequal.

        Checking accuracy
            The parameter for the checking type.

        Points to check
            The number of comparisons to make between the student's answer and the correct answer.

        Maximum no. of failures
            If the comparison fails this many times or more, the student's answer is marked as wrong.

        Checking range start
            The minimum value sample points can take.

        Checking range end
            The maximum value sample points can take.


This part type provides the following properties to the :data:`settings` object:

.. data:: correctAnswer
    :noindex:

    The :term:`Correct answer` to the question. 

.. data:: checkingType

    The :term:`Checking type` setting, representing the name of the checking function to use.
    One of ``"absdiff"``, ``"reldiff"``, ``"dp"`` or ``"sigfig"``.
    See :func:`resultsequal`.

.. data:: checkingAccuracy

    See :term:`Checking accuracy`. 

.. data:: failureRate

    See :term:`Maximum no. of failures`.

.. data:: vsetRangeStart

    See :term:`Checking range start`.

.. data:: vsetRangeEnd

    See :term:`Checking range end`.

.. data:: vsetRangePoints

    See :term:`Points to check`.

.. data:: maxLength

    The maximum length, in characters, of the student's answer, as set in :term:`Maximum length restriction`.

.. data:: maxLengthPC

    The proportion of credit awarded if the student's answer is too long.

.. data:: maxLengthMessage

    Message to add to marking feedback if the student's answer is too long.

.. data:: minLength

    The minimum length, in characters, of the student's answer, as set in :term:`Minimum length restriction`.

.. data:: minLengthPC

    The proportion of credit to award if the student's answer is too short.

.. data:: minLengthMessage

    Message to add to the marking feedback if the student's answer is too short.

.. data:: mustHave

    A list of strings which must be present in the student's answer, as set in :term:`Required strings`.

.. data:: mustHavePC

    The proportion of credit to award if any must-have string is missing.

.. data:: mustHaveMessage

    Message to add to the marking feedback if the student's answer is missing a must-have string.

.. data:: mustHaveShowStrings

    Tell the students which strings must be included in the marking feedback, if they're missing a must-have?

.. data:: notAllowed

    A list of strings which must not be present in the student's answer, as set in :term:`Forbidden strings`.

.. data:: notAllowedPC

    The proportion of credit to award if any not-allowed string is present.

.. data:: notAllowedMessage

    Message to add to the marking feedback if the student's answer contains a not-allowed string.

.. data:: notAllowedShowStrings

    Tell the students which strings must not be included in the marking feedback, if they've used a not-allowed string?

