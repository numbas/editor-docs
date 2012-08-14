Question reference
==================

A complete reference for every bit of the question edit page (apart from parts; see :doc:`question-parts`)

Admin buttons
=============

.. glossary::

    Switch to simplified/advanced editing mode
        In simplified editing mode, some properties are hidden. We're going to work on this a bit more with the aim of presenting a really simple interface for non-technical users who just want to take an existing question and make minimal changes like rewording the statement.

    Test Run
        Opens a preview of the question in a new window.

        .. warning:: 
            Do **NOT** use this link to deliver the question to students. It will put considerable load on the server. 
            Instead, download the question and put it either on your own webspace or in a VLE.

    Delete
        Delete the question permanently from the database. The associated questions are not deleted - you must delete them individually, if you want them to be deleted too.

    Make a Copy
        Create a copy of the question. Use this to make changes to an question which does not belong to you.

    Download
        Links to download standalone packages of the question. 

        * **standalone .zip** - a compiled package of the question, ready to run anywhere without connecting to a VLE. 
        * **SCORM package** - a compiled package of the question with SCORM files included, so it can be uploaded to a VLE and communicate with its gradebook.
        * **source** - a plain-text representation of the question, to be used with the Numbas command-line tools.


Metadata
========

.. glossary::

    Name
        The name of the question. This is shown to the student and used for searching within the editor, so make it something intelligible.

    Tags
        Use tags to categorise your questions. It's a good idea to use tags for the subject areas covered by the question, the difficulty level, and so on. If a word has more than one form, or commonly-used synonyms, for example "differentiation" and "derivative", then use them all so that the question will turn up in search results no matter which variation is used.

        To use the tag entry box: press the enter key to save a tag, and click on saved tags to edit them.

    Description
        Use this field to describe the question's contents, what it assesses, and so on. This is shown in the questions index, so make sure it's fairly concise.

    Author's Notes
        Use this field to record notes for yourself or other authors about the design of the question.

    Extensions
        Extensions can provide new functionality, such as extra JME functions or content types. To use an extension, tick its checkbox here.

Statement
========

The statement is a :ref:`content-area` which should can be used to give information setting up the entire question.

Rulesets
========

Variables
=========

Functions
=========

Parts
=====

See :ref:`question-parts`

Advice
======
