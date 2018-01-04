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
Settings can be used to set up the :ref:`answer input <custom-part-type-answer-input>` and in the :ref:`marking algorithm <custom-part-type-marking-algorithm>`.


