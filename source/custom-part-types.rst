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

Part settings
=============

Define setting fields to allow question authors to configure your part type.
They appear in the question editor's :guilabel:`Marking settings` tab for any parts of this type.

Settings can be used to set up the part type's :ref:`answer input <custom-part-type-answer-input>` and in the :ref:`marking algorithm <custom-part-type-marking-algorithm>`.

The following fields are common to all setting types:

.. glossary::

    Name
        A short name for this setting, used to refer to it in the part type's :ref:`answer input <custom-part-type-answer-input>` or :ref:`marking algorithm <custom-part-type-marking-algorithm>`.
        The name should uniquely identify the setting, but doesn't need to be very descriptive - the label can do that.
        A setting with name ``correct_answer`` will be available as ``settings["correct_answer"]``.

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
If :guilabel:`Substitute values into value` is ticked, then JME expressions enclosed in curly braces will be evaluated and the results substituted back into the expression.


