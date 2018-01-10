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

The student's answer is available inside the :ref:`marking script <custom-part-type-marking>` as :data:`studentAnswer`.

The following fields are common to all input methods:

.. glossary::

    Expected answer
        A JME expression which evaluates to the expected answer to the part.

    Input hint
        A string displayed next to the input field, giving any necessary information about how to enter their answer.

        If there are any requirements the student's answer must meet that aren't obvious from the way the input is displayed, for example a maximum length or required number of decimal places, these should be described here.

.. _custom-part-type-answer-input-methods:

Answer input methods
--------------------

.. glossary::

    String
        The student enters a single line of text.

        :data:`studentAnswer` is a :data:`string`.

    Number
        The student enters a number, using the default number notation style.
        
        :data:`studentAnswer` is a :data:`number`, as interpreted by :func:`parsenumber`.
        If the student's answer is not a valid representation of a number, ``NaN`` is returned.

        If you wish to allow other :ref:`number-notation` styles, a string input is more appropriate, so you can parse the student's answer yourself in the marking script.

    Mathematical expression
        The student enters a JME expression.
        A LaTeX rendering of the expression is displayed beside the input field.
        
        If the student's answer is not a valid expression, the part can not be submitted.
        
        :data:`studentAnswer` is an :data:`expression` value corresponding to the student's input.

    Matrix
        The student enters a numerical matrix.

        :data:`studentAnswer` is a :data:`matrix` value corresponding to the student's input.
    
    Radio buttons
        The chooses one from a list of choices by selecting a radio button.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        :data:`studentAnswer` is the index of the student's choice in the list. 
        The first item in the list is index 0.

    Choose several from a list
        The chooses any number of items from a list of choices by ticking checkboxes.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        :data:`studentAnswer` is a list of the indices of the student's choices in the list. 
        The first item in the list is index 0.

    Drop-down box
        The chooses one from a list of choices in a drop-down box.

        The :guilabel:`Choices` field should evaluate to a list of strings which will be shown to the student.

        :data:`studentAnswer` is the index of the student's choice in the list. 
        The first item in the list is index 0.


.. _custom-part-type-marking:

Marking
=======

The :guilabel:`Marking` tab is where you construct the :ref:`marking algorithm <marking-algorithm>` for your part type.

The interface is similar to that for :ref:`question variables <variables>` - a list of defined notes is shown on the right-hand side, and the currently selected note is shown on the left.

The two required notes, :data:`mark` and :data:`interpreted_answer`, can not be deleted.

.. glossary::

    Name
        The name of the note. 
        This must be a valid :ref:`JME variable name <variable-names>`.

    Definition
        A :ref:`jme` expression used to evaluate the note.

    Description
        Describe what the note means, and how it is used.

        You should try to describe the value the note produces, as well as any feedback.

        .. note::
            Don't underestimate the value of the description field!
            Notes whose meaning seems clear when you write them have a habit of becoming indecipherable months later.

    Depends on
        A list of all notes used in this note's definition.
        You can click on a note's name to go to its definition.
        If the note hasn't been defined yet, it'll be created.

    Used by
        A list of all notes which use this note in their definition. 
        You can click on a note name to go to its definition.
