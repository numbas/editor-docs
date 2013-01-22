Question reference
******************

A complete reference for every bit of the question edit page (apart from parts; see :doc:`question-parts`)

Admin buttons
=============

.. glossary::
    Test Run
        Opens a preview of the question in a new window. A specially simplified theme will be used, different from the one used for exams.

        .. warning:: 
            Do **NOT** use this link to deliver the question to students. It will put considerable load on the server. 
            Instead, download the question and put it either on your own webspace or in a VLE.

    Delete
        Delete the question permanently from the database.

    Make a Copy
        Create a copy of the question and edit that instead. Use this to make changes to a question which does not belong to you.

    Download
        Links to download standalone packages of the question. 

        * **standalone .zip** - a compiled package of the question, ready to run anywhere without connecting to a VLE. 
        * **SCORM package** - a compiled package of the question with SCORM files included, so it can be uploaded to a VLE and communicate with its gradebook.
        * **source** - a plain-text representation of the question, to be used with the Numbas command-line tools.


General
========

.. glossary::
    Question name
        The name of the question. This is shown to the student and used for searching within the editor, so make it something intelligible.

    Description
        Use this field to describe the question's contents, what it assesses, and so on. This is shown in the questions index and in the questions list of any exams containing this question, so make sure it's fairly concise.

    Author's Notes
        Use this field to record notes for yourself or other authors about the design of the question.

    Extensions
        Extensions can provide new functionality, such as extra JME functions or content types. To use an extension, tick its checkbox here.

    Tags
        Use tags to categorise questions so they can be found through the search function. Your guiding principle should be "more is better" - try to write down all words that someone searching for this question might use.

        After typing a tag in the box, press the Enter key to add it to the list. You can click on an existing tag to edit or remove it.

Statement
=========

The statement is a :ref:`content-area` which appears at the top of the question, before any input boxes. Use the statement to set the question and provide any information the student needs to answer it.


Variables
=========

Variables are defined using :doc:`jme-reference` syntax. 

The :guilabel:`Computed value` column shows a generated value for each variable. Note that when the question is delivered to students, the variable values are generated with each new attempt, so students won't necessarily see the same values as those displayed here. It's a good idea to use the :guilabel:`Regenerate values` button a few times to check that randomised variables don't take unsuitable values.

You can reorder the variables in the list by dragging the arrow icons. Doing this doesn't affect the way values are computed.

Functions
=========

If you need to do something a bit more complicated with variables, or you find yourself repeating the same pattern over and over, you can define a custom function. Custom functions can be used in any JME expression in the question, such as variable definitions or part answers.

.. glossary::
    Name
        The name of the function. Should be a valid JME name - it should start with a letter, and contain only letters and numbers, with no spaces or punctuation.

    Language
        Functions can be defined either with a JME expression or with JavaScript code. In the case of a JME expression, the value returned is the result of evaluating the expression on the function's parameters. You can also refer to the question's variables.

        JavaScript functions should return their result with a ``return`` expression. You don't need to write the ``function(parameters) {}`` part - just write the function body.

    Output type
        The type of the value returned by the function. 

    Parameters
        The parameters given to the function. You can refer to them by name in the function's definition. Make sure you correctly set the types of the parameters. You can define several functions with the same name but different parameter types, if it makes sense to do so.

    Rulesets
        A "ruleset" defines a list of named :doc:`simplification` used to manipulate mathematical expressions.

Parts
=====

See the page on :ref:`question-parts`.

Advice
======

:guilabel:`Advice` is a :ref:`content-area` which is shown when the student presses the :guilabel:`Reveal` button to reveal the question's answers, or when they receive less than the exam's :term:`Advice threshold` after submitting their answers.

The advice area is normally used to present a worked solution to the question.
