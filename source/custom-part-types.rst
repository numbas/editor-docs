.. _custom-part-types:

Custom part types
*****************

Custom part types allow you to reuse marking algorithms you've written, while providing fields for the part's settings, like the built-in parts.

Creating a new part type
========================

To create a new custom part type, click on your user icon at the top of the page, and then :guilabel:`Profile`.
Once on your profile, click :guilabel:`Part types`, and then :guilabel:`Create a new part type`.

The first step is to pick a name for your part type.
It should concisely describe what the part type is for, ideally by describing how the student should answer it or how it is marked.
For example, "Give a root of a function" is a good name for a part type where the student has to provide a value which is mapped to zero by a function defined by the question author.

You can change the name of your part type later on if you need to.

The part type editor
====================

The editing interface for custom part types is arranged similarly to the question and exam editors: the sections are separated into tabs, and you should work through them all in order to define how the part type works.

Description
===========

.. glossary::

    Name
        The name of the part type as it appears in the question editor. 
        It should concisely describe what the part type is for, ideally by describing how the student should answer it or how it is marked.
        For example, "Give a root of a function" is a good name for a part type where the student has to provide a value which is mapped to zero by a function defined by the question author.

    Description
        Use this field to describe how this part type works, and what kinds of questions it is appropriate for. 
        This text will appear in the list of part types on your profile, and in the public list if you make your part type public, to help question authors decide if the part type is right for their use.

.. _custom-part-type-settings:

Part settings
=============

Define setting fields to allow question authors to configure your part type.
They appear in the question editor's :guilabel:`Marking settings` tab for any parts of this type.

Each setting produces a JME value which can be used to set up the part type's :ref:`answer input <custom-part-type-answer-input>` and in the :ref:`marking algorithm <custom-part-type-marking>`.
For example, a setting with name ``correct_answer`` will be available as ``settings["correct_answer"]``.

The following fields are common to all setting types:

.. glossary::

    Name
        A short name for this setting, used to refer to it in the part type's :ref:`answer input <custom-part-type-answer-input>` or :ref:`marking algorithm <custom-part-type-marking>`.
        The name should uniquely identify the setting, but doesn't need to be very descriptive - the label can do that.

    Label
        The label shown next to the setting in the question editor.
        Try to make it as clear as possible what the setting is for.
        For example, a checkbox which dictates whether an input hint is shown should be labelled something like "Hide the input hint?" rather than "Input hint visibility" - the latter doesn't tell the question author whether ticking the checkbox will result in the input hint appearing or not.

    Help URL
        The address of documentation explaining this setting in further depth.
        This is optional.

    Input hint for question author
        Use this field to give further guidance to question authors about this setting, if the label is not enough.
        For example, you might use this to say what data type a JME code setting should evaluate to.

    Default value
        The initial value of the setting in the question editor.
        If the setting has a sensible default value, set it here.
        If the value of the setting is likely to be different for each instance of this part type, leave this blank.
        (Not present for :guilabel:`Drop-down box` or :guilabel:`Choose one or more` 

Setting types
-------------

String
######

A string of text. 
If :guilabel:`Substitute values into text` is ticked, then JME expressions enclosed in curly braces will be evaluated and the results substituted back into the text when the question is run.
Otherwise, the string will be untouched.

Mathematical expression
#######################

A mathematical expression, in :ref:`JME` syntax.
If :guilabel:`Substitute variables into value?` is ticked, then JME expressions enclosed in curly braces will be evaluated and the results substituted back into the string.

This setting type produces a value of type :data:`expression`.

Checkbox
########

If the question author ticks the checkbox, this setting type produces ``true``, otherwise it produces ``false``.

Drop-down box
#############

The question author must pick one option from a list that you provide. 
The :guilabel:`Label` field is shown to the question author, and the setting produces the :guilabel:`Value` field as a string.

Choose one or more
##################

The choices are presented to the question author as a list, with a checkbox next to each label.
This setting type produces a list containing the :guilabel:`Value` fields of ticked choices, as strings.

If :guilabel:`Default on?` is ticked for a particular choice, that choice is selected when a new part of this type is created.

JME code
########

A code editing area for the question author to write a JME expression.

If :guilabel:`Evaluate?` is ticked, the expression will be evaluated when the question is run, and the setting produces the resulting value.
The evaluation happens inside the question's scope, so any variables and functions defined by the question author are substituted in before evaluation.

If :guilabel:`Evaluate?` is not ticked, this setting will produce a :data:`expression` value representing the question author's expression.

.. _custom-part-type-answer-input:

Percentage
##########

A sliding scale between 0% and 100%.

This setting type produces a number between 0 and 1.

HTML content
############

An HTML :ref:`content area <content-areas>`.

If :guilabel:`Substitute variables into value?` is ticked, then JME expressions enclosed in curly braces will be evaluated and the results substituted back into the text.

List of strings
###############

This setting type produces a list of strings entered by the question author.

If :guilabel:`Substitute variables into value?` is ticked, then JME expressions enclosed in curly braces in each string will be evaluated and the results substituted back in.

Answer input
============

The answer input method determines how the student enters their answer to the part.

The student's answer is available inside the :ref:`marking script <custom-part-type-marking>` as ``studentanswer``.

The following fields are common to all input methods:

.. glossary::

    Expected answer
        A JME expression which evaluates to the expected answer to the part.

    Input hint
        A string displayed next to the input field, giving any necessary information about how to enter their answer.

        If there are any requirements the student's answer must meet that aren't obvious from the way the input is displayed, for example a maximum length or required number of decimal places, these should be described here.

Answer input methods
--------------------

.. glossary::

    String
        The student enters a single line of text.

    Number
        The student enters a number, using the default number notation style.
        ``studentanswer`` is a :data:`number`, as interpreted by :func:`parsenumber`.
        If the student's answer is not a valid representation of a number, ``NaN`` is returned.

        If you wish to allow other :ref:`number-notation` styles, a string input is more appropriate, so you can parse the student's answer yourself in the marking script.

    Mathematical expression
        The student enters a JME expression.
        A LaTeX rendering of the expression is displayed beside the input field.
        ``studentanswer`` is an :data:`expression` value corresponding to the student's input.
        If the student's answer is not a valid expression, the part can not be submitted.

    Matrix
        The student enters a numerical matrix.

        ``studentanswer`` is a :data:`matrix` value corresponding to the student's input.
    
    Radio buttons
        The chooses one from a list of choices by selecting a radio button.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        ``studentanswer`` is the index of the student's choice in the list. 
        The first item in the list is index 0.

    Choose several from a list
        The chooses any number of items from a list of choices by ticking checkboxes.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        ``studentanswer`` is a list of the indices of the student's choices in the list. 
        The first item in the list is index 0.

    Drop-down box
        The chooses one from a list of choices in a drop-down box.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        ``studentanswer`` is the index of the student's choice in the list. 
        The first item in the list is index 0.


.. _custom-part-type-marking:

Marking
=======

The :dfn:`marking algorithm` is responsible for:

    * Rejecting the student's answer if it's invalid. 
      If the answer is rejected, no credit or feedback will be given and the student must change their answer before resubmitting.
    * If the student's answer is valid, assigning credit and giving feedback messages.

The :dfn:`credit` for a part is the proportion of the marks available which should be awarded to the student.
The total marks available are set by the question author, and might be reduced if the student reveals :term:`steps`, or if this part is a gap in a :ref:`gap-fill <gap-fill>` part.

The :dfn:`feedback messages` shown to the student are strings of text shown after the part has been marked.
These might only become visible to the student after they have finished the exam, so don't rely on feedback messages to convey information that students might need in subsequent parts.

The marking algorithm comprises a set of :dfn:`marking notes`, which are evaluated similarly to :ref:`question variables <question-variables>`.
Two marking notes are required: ``mark`` and ``interpreted_answer``.

``mark`` should award credit and provide feedback based on the student's answer.
If the student's answer is invalid, ``mark`` should :func:`fail`. 

``interpreted_answer`` should produce a value representing the student's answer to this part, which can be used by other parts with :ref:`adaptive marking <adaptive-marking>`.

Each note evaluates to a value, and also produces a list of :dfn:`feedback items`, which modify the amount of credit awarded or give a message to the student. 
When a feedback item modifies the amount of credit awarded, a message describing the number of marks awarded or taken away from the previous total is displayed to the student.

If a note fails, either because it applies the :func:`fail` function or an error is thrown while it is evaluated, it will produce no value and no feedback items.
Any notes referring to a failed note also fail.
If the ``mark`` or ``interpreted_answer`` notes fail, the student's answer is rejected and the student must change their answer before resubmitting.

Like question variables, marking notes can refer to each other.
When another note is referred to in another note's definition, its value is substituted in.
To apply another note's feedback items, use :func:`apply`.

.. _jme-marking-functions:

Marking-specific JME functions
------------------------------

All the built-in :ref:`JME functions <jme-functions>` are available in marking notes, as well as the following functions specifically to do with marking:

.. function:: correct(message)

    Set the credit to 1 and give the feedback message ``message``. 
    If ``message`` is omitted, the default "Your answer is correct" message for the current locale is used.

.. function:: incorrect(message)

    Set the credit to 0 and give the feedback message ``message``. 
    If ``message`` is omitted, the default "Your answer is incorrect" message for the current locale is used.

.. function:: set_credit(credit, message)

    Set the credit to ``credit``, and give the feedback message ``message``. 
    The message should explain why the credit was awarded.

.. function:: add_credit(credit, message)
    
    Add ``credit`` to the current total, to a maximum of 1, and give the feedback message ``message``. 
    The message should explain why the credit was awarded.

    If ``credit`` is negative, credit is taken away, to a minimum of 0.

.. function:: sub_credit(credit, message)

    Subtract ``credit`` from the current total and give the feedback message ``message``.
    The message should explain why the credit was taken away.

.. function:: multiply_credit(proportion, message)

    Multiply the current credit by ``proportion`` and give the feedback message ``message``.
    The message should explain why the credit was modified.

    This operation is displayed to the student as an absolute change in marks awarded, not a multiplication. 
    For example, if the student already had 2 marks and `multiply_credit(0.5,message)` was applied, the message displayed would be along the lines of "1 mark was taken away".

.. function:: end()

    End the marking here. 
    Any feedback items produced after this one are not applied.

    This is most useful as a way of stopping marking once you've decided the student's answer is incorrect partway through a multi-step marking process.

.. function:: fail(message)

    Reject the student's answer as invalid, set the credit to 0 and give the feedback message ``message``.
    The message should explain why the student's answer was rejected.

    Since the student might not see the feedback message until the exam is over, you should also use :func:`warn` to add a warning message next to the input field describing why the student's answer was rejected.

.. function:: feedback(message)

    Give the feedback message ``message``, without modifying the credit awarded.

.. function:: x ; y

    Add feedback items generated by ``x`` to those generated by ``y``, and return ``y``.

    This is a way of chaining multiple feedback items together.

    **Example**:
        * ``incorrect() ; end()`` - mark the student's answer as incorrect, then end marking.
        * ``apply(note1) ; apply(note2)`` - apply feedback generated by ``note1``, then feedback generated by ``note2``.

.. function:: apply(feedback)

    If ``feedback`` is the name of a marking note, apply its feedback items to this note.

    If ``feedback`` is a list of feedback items generated by a function such as :func:`submit_part`, apply them to this note.

    **Examples**:
        * ``apply(validNumber)`` - add the feedback from the note ``validNumber`` to this note.
        * ``apply([submit_part(gaps[0]["path"]), submit_part(gaps[1]["path"])])`` - mark the first two gaps and add their feedback to this note.

.. function:: apply_marking_script(name, studentanswer, settings, marks)

    Apply the marking script with the given name, with the given values of the variables ``studentanswer`` and ``settings`` and with ``marks`` marks available.

    Any feedback items generated by the marking script are applied to this note.

    The built-in marking scripts are stored in the `marking_scripts <https://github.com/numbas/Numbas/tree/master/marking_scripts>`_ folder of the Numbas source repository.
    Use the name of the script without the ``.jme`` extension as the ``name`` parameter of this function.

    **Example**:
        * ``apply_marking_script("numberentry",studentAnswer,settings+["minvalue":4,"maxvalue":5],1)`` - mark this part using the :ref:`number entry <number-entry>` part's marking script, but with the minimum and maximum accepted values set to 4 and 5.

.. function:: submit_part(path)

    Submit the part with the given path. 
    Returns a dictionary of the following form::

        [
            "answered": has the student given a valid answer to the part?,
            "credit": credit awarded for the part,
            "marks": number of marks awarded,
            "feedback": feedback items generated by the part's marking algorithm
        ]

    Custom part types can't depend on other parts being available. 
    However, you might want to allow the question author to provide the path of another part, or do something with this part's gaps or steps, whose paths are listed in :data:`gaps` and :data:`steps`.

.. function:: mark_part(path, studentanswer)
    
    Mark the part with the given path, using the given value for ``studentanswer``.

    Returns a dictionary of the following form::

        [
            "valid": is the given answer a valid answer to the part?,
            "credit": credit awarded for the part,
            "marks": number of marks awarded,
            "feedback": feedback items generated by the part's marking algorithm,
            "states": a dictionary mapping the name of each marking note to a list of feedback items,
            "state_valid": a dictionary mapping the name of each marking note to a boolean representing whether that note failed,
            "values": a dictionary mapping the name of each marking note to its value
        ]

    This function is most useful in a custom marking algorithm for a gap-fill part, when you want to reassign the student's answers to each of the gaps.
    For example, in a part with two number entry gaps, you could ensure that the lowest answer is marked by the first gap, and the highest answer is marked by the second.
    This would allow the student to enter their answers in any order, and the question author to set the expected answer for the first and second gaps to the lowest and highest correct answers, respectively.

.. function:: concat_feedback(items,scale)

    Apply the given list of feedback items (generated by :func:`submit_part` or :func:`mark_part`) to this note, scaling the credit awarded by ``scale``.

    **Example**:
        * Mark gap 0, and award credit proportional to the number of marks available::

            let(result,mark_part(gaps[0]["path"],studentanswer[0]),
                concat_feedback(result["feedback"], result["marks"])
            )
