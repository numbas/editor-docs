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

        Allow the student to enter a fraction?
            This option is only available when no precision restriction is applied, since they apply to decimal numbers. If this is ticked, the student can enter a ratio of two whole numbers, e.g. ``-3/8``, as their answer.

        Require trailing zeroes?
            This option only applies when a precision restriction is selected. If this is ticked, the student must add zeroes to the end of their answer (when appropriate) to make it represent the correct precision. For example, consider a part whose correct answer is :math:`1.4`, and you want the student's answer to be correct to three decimal places. If "Require trailing zeroes?" is ticked, only the answer :math:`1.400` will be marked correct. If it is not ticked, any of :math:`1.4`, :math:`1.40` or :math:`1.400` will be marked as correct. If *too many* zeroes are used, e.g. :math:`1.4000`, the answer is marked as incorrect.
            
        Show precision restriction hint?
            If this is ticked, then some text describing the rounding the student must perform is shown next to the input box. For example, "round your answer to 3 decimal places".

        Display the correct answer as a fraction?
            This option is only available when no precision restriction is applied. If this is ticked, the correct answer to the part will be rendered as a fraction of two whole numbers instead of a decimal. For example, if the answer is :math:`0.5`, it will be displayed as ``1/2`` instead of ``0.5``.

        Allowed notation
            The styles of number notation that the student can use to enter their answer.
            There are different ways of writing numbers, based on culture and context.
            Tick an option to allow the student to use that style in their answer.
            Note that some styles conflict with each other: for example, ``1.234`` is a number between 1 and 2 in English, while it's the integer 1234 in French. 
            The student's answer will be interpreted using the first allowed style for which it is a valid representation of a number.
            See :ref:`number-notation` for more on styles of notation.

        Correct answer style
            The style of number notation to use when displaying the student's answer.

