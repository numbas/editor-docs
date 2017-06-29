.. _multiple-choice:

Choose one from a list / Choose several from a list / Match choices with answers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are three kinds of "multiple response" part types in Numbas, with similar settings.
They are listed here together.

.. topic:: Multiple response part types

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
            For :term:`choose several from a list` and :term:`match choices with answers` parts, the student must select at least this many choices. The value 0 means "no minimum", though the student must make at least one choice to submit the part.

        Maximum answers
            For :term:`choose several from a list` and :term:`match choices with answers` parts, the student must select at most this many choices. The value 0 means "no maximum".

        What to do if wrong number of answers selected
            If the student selects too few or too many answers, either do nothing, show them a warning but allow them to submit, or prevent submission until they pick an acceptable number of answers.

        Shuffle order of choices?
            If this is ticked, the choices are displayed in random order.

        Shuffle order of answers? (:term:`Match choices with answers` only)
            If this is ticked, the answers are displayed in random order.

        Number of display columns
            For :term:`choose one from a list` and :term:`choose several from a list` parts, this dictates how many columns the choices are displayed in. If 0, the choices are displayed on a single line, wrapped at the edges of the screen.

        Selection type
            For :term:`match choices with answers` parts, "One from each row" means that the student can only select one answer from each row and "Checkboxes" means that the student can select any number of choice-answer pairs.

            For :term:`choose one from a list` parts, users can select only one of the choices. 

            "Drop down list" means that the choices are shown as a selection box; the student can click to show the choices in a vertical list.

            .. figure:: images/dropdown.png
                :alt: A dropdown list showing some choices

            .. warning::
                Drop down lists can only display plain text, due to how selection boxes are implemented in HTML. 
                This means that any formatting applied in the editor will not be displayed, and LaTeX will not render properly.

            "Radio buttons" means that choices are shown separately, in-line with the part prompt.

            .. figure:: images/radiobuttons.png
                :alt: A list of choices with radio buttons

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

