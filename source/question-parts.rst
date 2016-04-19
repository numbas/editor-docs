.. _question-parts:

Question parts
==============

Each question has one or more parts. Parts are listed on the left of the screen; click on a part's entry in the list to edit it.

The part currently being edited can be moved up and down the order by clicking the blue arrows to the right of the list.

Generic part properties
-----------------------

.. glossary::
    Prompt
        A content area used to prompt the student for an answer.

    Marks
        The number of marks to award for answering the part correctly.

    Steps
        An optional list of sub-parts which the student can reveal by clicking on a button. Marks awarded for steps don't increase the total available for the part, but are given in case the student gets a lower score for the main part.

    Penalty for revealing steps
        If the student reveals the Steps, reduce the total available marks by this amount. Credit for the part is scaled down accordingly. For example, if there are 6 marks available and the penalty for revealing steps is 2 marks, the total available after revealing steps is 4. An answer worth 3 marks without revealing steps is instead worth :math:`3 \times \frac{4}{6} = 2` marks after revealing steps.

    Show correct answer on reveal?
        When the student reveals answers to the question, or views the question in review mode, should a correct answer be shown? You might want to turn this off if you're doing custom marking and the part has no "correct" answer.

.. _part-scripts:

Scripts
-------

The script fields allow you to override the built-in algorithms used by Numbas. They take JavaScript code; `the Numbas JavaScript API documentation for parts <http://numbas.github.io/Numbas/Numbas.parts.Part.html>`_ is a useful reference.

Scripts have access to the global ``Numbas`` object, as well as the following variables:

.. attribute:: part

    The current part

.. attribute:: question

    The part's parent question

.. attribute:: variables

    The question's variables, unwrapped to JavaScript objects (so numbers can be used as JavaScript numbers, instead of having to go through the JME system)

The following scripts can be customised:

.. glossary::

    When the part is created
        This function runs when the part is created (either at the start of the exam, or when the question is regenerated), after the built-in constructor for the part. 
        You could use this to change any of the part's settings, if it's not convenient to do so by other means.

    Mark student's answer
        This function runs when the student clicks the :guilabel:`Submit part` button. 
        It should establish what proportion of the available credit to award to the student for their answer, and give feedback messages. 
        Use ``this.setCredit(credit,message)`` to set the credit and (optionally) give a message. 
        Note that ``this.answered`` should be set to true if the student's answer can be marked - otherwise, the student will be shown a warning message.

    Validate student's answer
        This functions runs after the marking function, and should return ``true`` if the student's answer is in a form that can be marked, or ``false`` otherwise. 
        If the answer can't be marked, you should use ``this.giveWarning(message)`` to tell the student what's wrong.

There are several example questions using custom scripts at `numbas.mathcentre.ac.uk/exam/1016/custom-marking/ <https://numbas.mathcentre.ac.uk/exam/1016/custom-marking/>`_.

.. _adaptive-marking:

Adaptive marking
----------------

Adaptive marking allows you to incorporate the student's answers to earlier parts when marking their answer to another part.
You could use this to allow an "error carried forward" marking scheme, or in more free-form questions where one part has no correct answer - for example, "think of a number and find its square root".
This is achieved by replacing the values of question variables with the student's answers to other parts.
When a variable is replaced, any other variables depending on that one are recalculated using the new value.

.. warning::
    This can be very powerful, but make sure you don't introduce any new random variation in these dependent variables, or the correct answer will change each time the student submits their answer.

As an example, suppose part **a** of your question asks the student to calculate the mean of a set of numbers. 
The correct answer for this part is the variable ``sample_mean``.
Part **b** then asks the student to calculate a *z*-statistic based on the mean of the sample. 
The correct answer to this part is the variable ``z_statistic``, which is defined as ``(sample_mean-population_mean)/sqrt(population_variance)``.
(``population_mean`` and ``population_variance`` in this case are random numbers)

If the student makes an error in calculating the sample mean but uses the right method to find a *z*-statistic, they shouldn't be penalised in part **b**. 
We can ensure this by replacing the value of ``sample_mean`` with the student's answer to part **a** when marking part **b**.
When the student submits an answer to part **b**, the value of ``z_statistic`` will be automatically recalculated using the student's value of ``sample_mean``. 
Then, if the student correctly applies the formula, their answer will match the new value of ``z_statistic`` and they will receive full credit for the part.

.. topic:: Variable replacements

    .. glossary::

        Variable
            The name of the variable to replace

        Answer to use
            The part whose answer the variable's value should be replaced with. 
            Different part types produce different types of values.

        Must be answered?
            If this is ticked, the student must submit an answer to the referenced part before they can submit an answer to this part.

    There are two variable replacement strategies:

    .. glossary::

        Try without replacements first
            The student's answer is first marked using the original values of the question variables.
            If the credit given by this method is less than the maximum available, the marking is repeated using the defined variable replacements.
            If the credit gained with variable replacements is greater than the credit gained under the original marking, that score is used, and the student is told that their answers to previous parts have been used in the marking for this part.

        Always replace variables
            The student's answer is only marked once, with the defined variable replacements applied.

    .. _part_type_variable_replacement:

.. topic:: Values obtained from the answers to each part types

    =========================== ==============
    Part type                   Value obtained
    =========================== ==============
    Gap-fill                    A list containing the values obtained from each of the gaps
    Mathematical expression     A JME subexpression. 
                                When used in a variable definition, the subexpression will be substituted in, and any references to question variables in the subexpression will be replaced with their respective values.
    Number entry                A number
    Matrix entry                A matrix
    Match text pattern          A string
    Choose one from a list      The index of the answer the student chose
    Choose several from a list  A list of booleans: true if the student ticked the corresponding choice, false otherwise
    Match choices with answers  A 2D list of lists of boolean values, in the same format as a :term:`custom marking matrix` for this part - cells are addressed by choice first, and answer second.
    =========================== ==============

    The following screencast shows the addition of adaptive marking to a question:

    .. raw:: html

        <iframe src="https://player.vimeo.com/video/134209217" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Part types
----------

.. _information-only:

Information only
^^^^^^^^^^^^^^^^

An information part contains only a prompt and no answer input. It is most often used as a Step to provide a hint for a parent part.

.. _gap-fill:

Gap-fill
^^^^^^^^

Gap-fill parts allow you to include answer inputs inline with the prompt text, instead of at the end of the part.

The "gaps" are sub-parts. Include them in text by clicking on the :guilabel:`Insert gap` button on the toolbar, and entering the number of the gap you want to insert in the dialog box. You can double-click on a gap placeholder to change its number.

To insert a gap in the plain text editor, type the gap's number between two square brackets, e.g. `[[0]]` for the first gap.

.. _mathematical-expression:

Mathematical expression
^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^

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
            This option only applies when a precision restriction is selected. If this is ticked, the student must add zeroes to the end of their answer (when appropriate) to make it represent the correct precision. For example, consider a part whose correct answer is :math:`1.4`, and you want the student's answer to be correct to three decimal places. If "Require trailing zeroes?" is ticked, only the answer :math:`1.400` will be marked correct. If it is not ticked, any of :math:`1.4`, :math:`1.40` or :math:`1.400` will be marked as correct. If *too many* zeroes are used, e.g. :math:`1.4000`, the answer is marked as incorrect.

        Allow the student to enter a fraction?
            This option is only available when no precision restriction is applied, since they apply to decimal numbers. If this is ticked, the student can enter a ratio of two whole numbers, e.g. ``-3/8``, as their answer.

        Display the correct answer as a fraction?
            This option is only available when no precision restriction is applied. If this is ticked, the correct answer to the part will be rendered as a fraction of two whole numbers instead of a decimal. For example, if the answer is :math:`0.5`, it will be displayed as ``1/2`` instead of ``0.5``.

.. _matrix-entry:

Matrix entry
^^^^^^^^^^^^

Matrix entry parts ask the student to enter a matrix of numbers. Marks are awarded if every cell in the student's answer is equal to the corresponding cell in the correct answer, within the allowed margin of error.

.. topic:: Marking

    .. glossary::
        Correct answer
            The expected answer to the part. This is a JME expression which must evaluate to a :data:`matrix`.

        Display numbers in the correct answer as fractions?
            If this is ticked, then non-integer numbers in the correct answer will be displayed as fractions instead of decimals.

        Number of rows
            The default number of rows in the student's answer field.

        Number of columns
            The default number of columns in the student's answer field.

        Allow student to change size of matrix?
            If this is ticked, then the student can change the number of rows or columns in their answer. USe this if you don't want to give a hint about the dimensions of the answer.

        Margin of error allowed in each cell
            If the absolute difference between the student's value for a particular cell and the correct answer's is less than this value, then it will be marked as correct.

        Gain marks for each correct cell?
            If this is ticked, the student will be awarded marks according to the proportion of cells that are marked correctly. If this is not ticked, they will only receive the marks for the part if they get every cell right. If their answer does not have the same dimensions as the correct answer, they are always awarded zero marks.

        Precision restriction
            You can insist that the student gives their answer to a particular number of decimal places or significant figures. For example, if you want the answer to be given to 3 decimal places, :math:`3.1` will fail this restriction, while :math:`3.100` will pass. If the precision doesn't matter, select :guilabel:`None`.

        Require trailing zeroes?
            This option only applies when a precision restriction is selected. If this is ticked, the student must add zeroes to the end of their answer (when appropriate) to make it represent the correct precision. For example, consider a part whose correct answer is :math:`1.4`, and you want the student's answer to be correct to three decimal places. If "Require trailing zeroes?" is ticked, only the answer :math:`1.400` will be marked correct. If it is not ticked, any of :math:`1.4`, :math:`1.40` or :math:`1.400` will be marked as correct. If *too many* zeroes are used, e.g. :math:`1.4000`, the answer is marked as incorrect.

        Allow the student to enter fractions?
            This option is only available when no precision restriction is applied, since they apply to decimal numbers. If this is ticked, the student can enter a ratio of two whole numbers, e.g. ``-3/8``, as their answer.

.. _match-text-pattern:

Match text pattern
^^^^^^^^^^^^^^^^^^

Use a text pattern part when you want the student to enter short, non-mathematical text.

.. topic:: Marking

    .. glossary::
        Answer pattern
            A `regular expression <https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Regular_Expressions>`_ defining the strings to be accepted as correct. If you just want to accept a single string, just writing it out here should work. If there are several valid answers, separate them with a ``|`` character.
            You can substitute variables, the same as in content areas, by enclosing expressions in curly braces, e.g. ``{answervar}``. If you're using the full regular expression functionality, note that ``^`` and ``$`` are automatically added to the start and end of the answer pattern to ensure that the student's whole answer matches the pattern.

        Display answer
            A representative correct answer string to display to the student, in case they press the :guilabel:`Reveal answers` button. You can substitute variables by enclosing expressions in curly braces, the same as in content areas.

        Must the answer be in the correct case?
            If this is ticked, the capitalisation of the student's answer must match that of the answer pattern. If it doesn't, partial credit (defined using the slider below the checkbox) will be awarded.

.. _multiple-choice:

Choose one from a list / Choose several from a list / Match choices with answers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. glossary::

    Choose one from a list
        The student must choose one of several options

    Choose several from a list
        The student can choose any of a list of options

    Match choices with answers
        The student is presented with a 2D grid of :guilabel:`choices` and :guilabel:`answers`. Depending on how the part is set up, they must either match up each choice with an answer, or select any number of choice-answer pairs.


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

        What to do if wrong number of answers selected
            If the student selects too few or too many answers, either do nothing, show them a warning but allow them to submit, or prevent submission until they pick an acceptable number of answers.

        Shuffle order of choices?
            If this is ticked, the choices are displayed in random order.

        Shuffle order of answers? (:term:`Match choices with answers` only)
            If this is ticked, the answersare displayed in random order.

        Number of display columns
            For :term:`choose one from a list` and :term:`choose several from a list` parts, this dictates how many columns the choices are displayed in. If 0, the choices are displayed on a single line, wrapped at the edges of the screen.

        Selection type
            Only applies to :term:`match choices with answers` parts. "One from each row" means that the student can only select one answer from each row. "Checkboxes" means that the student can select any number of choice-answer pairs.

        Custom marking matrix
            If the checkbox is ticked, the :ref:`JME <jme>` expression in the box below is evaluated and used to assign numbers of marks to choices. 
        
        Custom matrix expression
            Define the number of marks to award for each of the choices. 
            For :term:`choose one from a list` and :term:`choose several from a list` parts, the expression should evaluate to a list of numbers, while for :term:`match choices with answers` it should evaluate to a list of lists of numbers representing a 2d array, or a matrix object, giving the number of marks to associate with each choice-answer pair.

        Layout (:term:`Match choices with answers` only)
            Define which choices are available to be picked. 
            If :guilabel:`Custom expression` is selected, give either a list of lists of boolean values, or a matrix with as many rows as the part has choices and as many columns as the part has answers. 
            Any non-zero value in the matrix indicates that the corresponding choice-answer pair should be available to the student.

.. _choices:
.. topic:: Choices

    .. glossary::
        Variable list of choices?
            Should the list of choices be defined by a JME expression? If this is ticked, you must give a :term:`custom matrix expression`.

        List of choices
            If :guilabel:`Variable list of choices?` is ticked, this JME expression defines the list of choice strings to display to the student. 

        Marks (:term:`choose one from a list` / :term:`choose several from a list` only)
            The number of marks to award (or take away, if you enter a negative number) when the student picks this choice.

        Distractor message (:term:`choose one from a list` / :term:`choose several from a list` only)
            A message to display to the student in the part's feedback section after they select a particular choice. 
            It can be useful to give some explanation of why a choice is incorrect.

.. _answers:
.. topic:: Answers (:term:`Match choices with answers` only)

    .. glossary::
        Variable list of answers?
            Should the list of answers be defined by a JME expression? If this is ticked, you must give a :term:`custom matrix expression`.

        List of answers
            If :guilabel:`Variable list of answers?` is ticked, this JME expression defines the list of answer strings to display to the student. 

.. _marking-matrix:
.. topic:: Marking matrix (:term:`Match choices with answers` only)

    Assign marks to each pair of choice and answer using the input boxes.
    
    .. glossary::
        Custom marking matrix
            If the checkbox is ticked, the :ref:`JME <jme>` expression in the box below is evaluated and used to assign numbers of marks to choices. 
        
        Custom matrix expression
            Define the number of marks to award for each of the choices. 
            Either a list of lists representing a 2d array, or a matrix object, giving the number of marks to associate with each choice-answer pair.
