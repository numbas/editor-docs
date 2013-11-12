.. _question-parts:

Question parts
==============

Each question has one or more parts. Parts are listed on the left of the screen; click on a part's entry in the list to edit it.

The part currently being edited can be moved up and down the order by clicking the blue arrows to the right of the list.

Generic part properties
-----------------------

.. glossary::
    Prompt
        A :ref:`content area <content-area>` used to prompt the student for an answer.

    Marks
        The number of marks to award for answering the part correctly.

    Steps
        An optional list of sub-parts which the student can reveal by clicking on a button. Marks awarded for steps don't increase the total available for the part, but are given in case the student gets a lower score for the main part.

    Penalty for revealing steps
        If the student reveals the Steps, reduce the total available marks by this amount. Credit for the part is scaled down accordingly. For example, if there are 6 marks available and the penalty for revealing steps is 2 marks, the total available after revealing steps is 4. An answer worth 3 marks without revealing steps is instead worth :math:`3 \times \frac{4}{6} = 2` marks after revealing steps.

.. _information-only:

Information only
----------------

An information part contains only a prompt and no answer input. It is most often used as a Step to provide a hint for a parent part.

.. _gap-fill:

Gap-fill
-------------

Gap-fill parts allow you to include answer inputs inline with the prompt text, instead of at the end of the part.

The "gaps" are sub-parts. Include them in text by writing their number (surrounded by double square brackets. For example, ``[[0]]`` inserts the first gap, and ``[[1]]`` includes the second one.

.. _mathematical-expression:

Mathematical expression
-----------------------

Mathematical expression parts require the student to enter an algebraic expression, using :ref:`JME <jme>` syntax.

These parts are marked by picking a sample of points uniformly from a given range for the free variables in the expression, and evaluating both the student's answer and the correct answer on those points. If the two expressions agree on enough inputs, then they are considered to be equivalent and the student's answer is marked as correct.

For questions where the student is asked to rearrange an expression, clearly just evaluating both answers won't detect the difference. For those cases, you can use a somewhat blunt method of string and length restrictions. We're working on a more sophisticated method.

Before length restrictions are applied, surplus brackets and whitespace are removed, and spaces are inserted between some operations, to minimise the possibility of the length restrictions being triggered for the wrong reasons.

.. topic:: Marking

    .. glossary::
        Correct answer
            The expected answer to the part. Question variables (or, more broadly, JME expressions which should be evaluated to a single value when the question is generated), can be included by enclosing them in curly braces.

        Show preview of student's answer?
            If ticked, a rendering of the student's answer in mathematical notation is displayed beeside the input box. You should leave this on unless you expect the answer to be veery simple and need the space - the feedback about how their answer is interpreted is very useful to students.

        Answer simplification rules
            :ref:`Simplification rules <simplification-rules>` to apply to the correct answer, if it is displayed to the student (for example, after clicking the :guilabel:`Reveal answers` button). This shouldn't affect marking.

.. _string-restrictions:

.. topic:: Accuracy and string restrictions

    .. glossary::
        Checking type
            The rule to use to compare the student's answer with the correct answer. In the lines below, :math:`x` represents the value of the student's answer at a particular point and :math:`y` represents the value of the correct answer, while :math:`\delta` is the value of the checking accuracy property.

            * Absolute difference. Fail if :math:`\left| x-y \right| > \delta`.
            * Relative difference. Fail if :math:`\left| \frac{x}{y} - 1 \right| > \delta`.
            * Decimal points. :math:`x` and :math:`y` are rounded to :math:`\delta` decimal places, and the test fails if the rounded values are unequal.
            * Significant figures. :math:`x` and :math:`y` are rounded to :math:`\delta` significant figures, and the test fails if the rounded values are unequal.

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

        Maximum length restriction
            If the student's answer contains more than this many characters, the penalty is applied. A value of zero means no restriction is applied. The student's answer is tidied up slightly so that things like extra or missing space characters don't affect the calculated length. All spaces are removed, and then spaces are inserted between binary operations. For example, the answer ``1+x`` (three characters) is marked as ``1 + x`` (five characters). 

        Minimum length restriction
            If the student's answer contains fewer than this many characters, the penalty is applied. A value of zero means no restriction is applied. See the comment above on how the length is calculated.

        Required strings
            If the student's answer doesn't contain all of these strings, the penalty is applied.

        Forbidden strings
            If the student's answer contains any of these strings, the penalty is applied.

        Warn if student uses an unexpected variable name?
            If this is ticked, all variable names used in the student's are checked against the list you provide. The first variable name which is not in the list will trigger a warning. You can use this option to prevent students incorrectly entering answers such as ``xy``, which is interpreted as a single variable, when they mean ``x*y``, the product of two variables.

        Expected variable names
            Variable names in this list will not prompt the "unexpected variable name" warning when the student uses them. 

.. _number-entry:

Number entry
------------

Number entry parts ask the student to enter a number, which is marked if it is in a specified range.

.. topic:: Marking

    .. glossary::
        Minimum accepted value
            The smallest value accepted as correct.

        Maximum accepted value
            The largest value accepted as correct.

        Must the answer be an integer?
            If this is ticked and the student's answer is not a whole number, the penalty is applied.

        Precision restriction
            You can insist that the student gives their answer to a particular number of decimal places or significant figures. For example, if you want the answer to be given to 3 decimal places, :math:`3.1` will fail this restriction, while :math:`3.100` will pass. If the precision doesn't matter, select :guilabel:`None`.

        Require trailing zeroes?
            This option only applies when a precision restriction is selected. If this is ticked, the student must add zeroes to the end of their answer (when appropriate) to make it represent the correct precision. For example, consider a part whose correct answer is :math:`1.4`, and you want the student's answer to be correct to three decimal places. If "Require trailing zeroes?" is ticked, only the answer `1.400` will be marked correct. If it is not ticked, any of `1.4`, `1.40` or `1.400` will be marked as correct. If *too many* zeroes are used, e.g. `1.4000`, the answer is marked as incorrect.

.. _match-text-pattern:

Match text pattern
------------------

Use a text pattern part when you want the student to enter short, non-mathematical text.

.. topic:: Marking

    .. glossary::
        Answer pattern
            A `regular expression <https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Regular_Expressions>`_ defining the strings to be accepted as correct. If you just want to accept a single string, just writing it out here should work. If there are several valid answers, separate them with a `|` character.
            You can substitute variables, the same as in content areas, by enclosing expressions in curly braces, e.g. ``{answervar}``. If you're using the full regular expression functionality, note that ``^`` and ``$`` are automatically added to the start and end of the answer pattern to ensure that the student's whole answer matches the pattern.

        Correct answer
            A representative correct answer string to display to the student, in case they press the :guilabel:`Reveal answers` button. You can substitute variables by enclosing expressions in curly braces, the same as in content areas.

.. _multiple-choice:

Choose one from a list / Choose several from a list / Match choices with answers
--------------------------------------------------------------------------------

.. topic:: Marking

    .. glossary::
        Minimum marks
            If the student would have scored less than this many marks, they are instead awarded this many. Useful in combination with negative marking.

        Maximum marks
            If the student would have scored more than this many marks, they are instead awarded this many. The value 0 means "no maximum mark".

        Minimum answers
            For :term:`choose several from a list` and :term:`match choices with answers` parts, the student must select at least this many choices.

        Maximum answers
            For :term:`choose several from a list` and :term:`match choices with answers` parts, the student must select at most this many choices.

        Shuffle order of choices?
            If this is ticked, the choices are displayed in random order.

        Number of display columns
            For :term:`choose one/several from a list` parts, this dictates how many columns the choices are displayed in. If 0, the choices are displayed on a single line, wrapped at the edges of the screen.

        Selection type
            Only applies to :term:`match choices with answers` parts. "One from each row" means that the student can only select one answer from each row. "Checkboxes" means that the student can select any number of choice-answer pairs.

        Custom marking matrix
            If the checkbox is ticked, the :ref:`JME <jme>` expression in the box below is evaluated and used to assign numbers of marks to choices. For :term:`choose one/several from a list` parts, the expression should evaluate to a list of numbers, while for :term:`match choices with answers` it should evaluate to a list of lists of numbers. 
        
        Marking matrix
            Define the choices available to the student and the number of marks to award for choosing them.

.. topic:: Choices (:term:`Choose one from a list` / :term:`Choose several from a list` only)

    .. glossary::
        Marks
            The number of marks to award (or take away, if you enter a negative number) when the student picks this choice.

        Distractor message
            A message to display to the student in the part's feedback section after they select a particular choice. Useful to give some explanation of why a choice is incorrect.

.. topic:: Marking matrix (:term:`Match choices with answers` only)
    
    Add answers and choices using the buttons, and assign marks using the input boxes.
