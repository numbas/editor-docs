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


