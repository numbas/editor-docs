Exam reference
**************

A complete reference for every bit of the exam edit page.

Undo/Redo
=========

You can undo or redo changes made since you opened the question editing page by clicking on the arrows at the top-right of the page.

Admin buttons
=============

.. glossary::
    Test Run
        Opens a preview of the exam in a new window.

        .. warning:: 
            Do **NOT** use this link to deliver the exam to students. It will put considerable load on the server. 
            Instead, download the exam and put it either on your own webspace or in a VLE.

    Feedback
        Use this button to give feedback about the quality of an exam, after test running it. The options are listed in descending order of "suitability for use":

        * **This is ready to use** - this exam is of sufficient quality to give to students.
        * **This should not be used** - this exam works, but you deprecate its use - for example, if it's not intended for use by students, or there's a better version elsewhere.
        * **This has some problems** - this exam works, but has some problems which mean it's not ready for use by students - for example, the exam is incomplete, or changes need to be made to the text. Further work is needed before this exam can be given to students.
        * **This doesn't work** - this exam doesn't even run!

    Delete
        Delete the exam permanently from the database. The associated questions are not deleted - you must delete them individually, if you want them to be deleted too.

    Make a Copy
        Create a copy of the exam. Use this to make changes to an exam which does not belong to you.

    Download
        Links to download standalone packages of the exam. 

        * **standalone .zip** - a compiled package of the exam, ready to run anywhere without connecting to a VLE. 
        * **SCORM package** - a compiled package of the exam with SCORM files included, so it can be uploaded to a VLE and communicate with its gradebook.
        * **source** - a plain-text representation of the exam, to be used with the Numbas command-line tools.

General
========

.. glossary::
    Exam name
        This is shown to the student and used for searching within the editor, so make it something intelligible.

    Licence
        You can specify the licence under which you are making your resources available. Different licences allow other users to copy, modify or reuse your content in differnet ways - consider which licence to choose carefully. *CC BY* allows other users to reuse your content however you like, as long as they give appropriate credit to you.

    Theme
        Themes control the user interface of an exam, changing the look and feel. The `default` theme is designed for exams which will be delivered over the web. There is also an experimental `worksheet` theme which can be used to print out multiple, randomised copies of an exam for students to complete on paper.

    Interface language
        Specify which translation to use for the text in the user interface, i.e. button labels, error messages, etc.

    Pass threshold
        Define a pass/fail threshold for the exam. The pass/fail message will be displayed when the student ends the exam. If set to zero, then no message is displayed.

    Description
        Use this field to describe the exam's contents, what it assesses, and so on. This is shown in the exams index, so make sure it's fairly concise.

    Author's notes
        Use this field to record notes for yourself or other authors about the design of the exam.

Navigation
==========

The navigation settings control how the student can move through the exam, and whether to give them warnings if they 

.. glossary::
    Allow user to regenerate questions?
        If ticked, then the :guilabel:`Try another question like this one` button is displayed at the bottom of each question, allowing the student to re-randomise the question and have another attempt at it.

    Allow move to previous question?
        If ticked, then the user is allowed to move back to a question after leaving it.

    Allow jump to any question?
        If ticked, then the user can jump between questions at will during the exam.

    Show front page?
        If ticked, then an intro screen is shown to the student before the exam starts, 

    Confirm before leaving the exam while it's running?
        If ticked, the student will be asked to confirm that they really want to leave if they try to close the exam while it's running, for example by pressing the browser's back button or closing the tab the exam is running in.

    On leaving a question
        What to do when the student changes question, or tries to end the exam. You can either warn the student and make them confirm that they'd like to leave, or prevent them from leaving the question entirely until they've answered it.

Timing
======

.. glossary::
    Exam duration
        The length of time students are allowed to attempt the exam. If set to zero, then there is no time limit.

    Allow pausing?
        If ticked, the student can pause the exam while running it, and the timer will stop. If unticked, there is no pause button, and the end time is fixed when the session starts - leaving and resuming through the VLE will not affect the end time.

    On timeout (event)
        If set to :guilabel:`Warn`, the given message is displayed when the student runs out of time.

    5 minutes before timeout (event)
        If set to :guilabel:`Warn`, the given message is displayed five minutes before the student runs out of time.

Feedback
========

.. glossary::
    Show current score?
        If ticked, the student will be shown their score for each question and part immediately after submitting their answers.

    Show maximum score?
        If ticked, the student will be shown the maximum attainable score for each question and part.

    Show answer state?
        If ticked, then when the student submits an answer an icon will be displayed to let the student know if their answer was marked correct, partially correct or incorrect.

    Allow reveal answer?
        If ticked, then the :guilabel:`Reveal answer` button is enabled on each question. If the student chooses to reveal the answer to a question, they are shown the correct answer but lose all their marks and can not re-attempt the question.

    Advice threshold
        If the student's score is below this threshold, then the question advice is displayed.

Events
======

Some of the properties described above are marked as *events*. These all have the same structure: an :guilabel:`action` setting which determines how to react to the event, and a :guilabel:`message` to display to the student when appropriate.

Questions
=========

.. glossary::

    Shuffle questions?
        If ticked, then the questions will be shown to the student in a random order. The order is randomised on each attempt.

    Use all questions?
        If ticked, then every question in the list will be shown to the student. If not, then only the number specified below will be used.

    Number of questions to display
        The number of questions to show to the student.

Select the questions to be included in the exam by searching for them in the box on the right-hand side and clicking the plus icon on questions you wish to use.

The order of questions can be rearranged by dragging and dropping questions using the up/down arrow handles on the left of each item.

Deleting a question from an exam does not remove it from the database. To permanently delete a question, click on its name and click the :guilabel:`Delete` button on the question's edit page.

Editing history
===============

Each time you make a change to a exam, it's saved to the database. You can see the full editing history of your exam in this tab, and revert back to a previous state by clicking on the :guilabel:`Restore` link.

You can add a comment describing what you've changed by clicking on the corresponding entry in the current version's :guilabel:`Comment` column. 

Each time somebody uses the :guilabel:`Feedback` button to provide feedback on the suitability for use of this exam, an entry is added to the editing history so you can see when the exam was last usable.

You and your co-authors can write general comments on a exam by clicking the :guilabel:`Write a comment` button.

Access
======

You can control who is allowed to see, and edit, your exams.

.. topic:: Public visibility

    .. glossary::

        Hidden
            Only you and users named in the :guilabel:`Individual access rights` section can see this exam.

        Anyone can see this
            Anyone, even users who are not logged in, can see this exam. Only you and users named in the :guilabel:`Individual access rights` section can edit this exam.

        Anyone can edit this
            Anyone, even users who are not logged in, can see and edit this exam.

.. topic:: Individual access rights

    Type a name into the search box to find a user. Click on a user's name in the results list to add them to the access list. Named users can have the following rights:

    .. glossary::

        Can view this
            The named user can see, but not edit, this exam.

        Can edit this
            The named user can see this exam and make changes to it.
