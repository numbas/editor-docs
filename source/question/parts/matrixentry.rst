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

