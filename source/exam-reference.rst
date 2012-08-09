Exam reference
**************

A complete reference for every bit of the exam edit page.

Admin buttons
=============

.. glossary::
    Test Run
        Opens a preview of the exam in a new window.

        .. warning:: 
            Do **NOT** use this link to deliver the exam to students. It will put considerable load on the server. 
            Instead, download the exam and put it either on your own webspace or in a VLE.

    Delete
        Delete the exam permanently from the database. The associated questions are not deleted - you must delete them individually, if you want them to be deleted too.

    Make a Copy
        Create a copy of the exam. Use this to make changes to an exam which does not belong to you.

    Download
        Links to download standalone packages of the exam. 

        * **standalone .zip** - a compiled package of the exam, ready to run anywhere without connecting to a VLE. 
        * **SCORM package** - a compiled package of the exam with SCORM files included, so it can be uploaded to a VLE and communicate with its gradebook.
        * **source** - a plain-text representation of the exam, to be used with the Numbas command-line tools.

Metadata
========

.. glossary::
    Name
        The name of the exam. This is shown to the student and used for searching within the editor, so make it something intelligible.

    Theme
        Themes control the user interface of an exam, changing the look and feel. The `default` theme is designed for exams which will be delivered over the web. There is also an experimental `worksheet` theme which can be used to print out multiple, randomised copies of an exam for students to complete on paper.

    Duration
        The length of time students are allowed to attempt the exam. If set to zero, then there is no time limit.

    Pass threshold
        Define a pass/fail threshold for the exam. The pass/fail message will be displayed when the student ends the exam. If set to zero, then no message is displayed.

    Shuffle questions?
        If ticked, then the questions will be shown to the student in a random order. The order is randomised on each attempt.

    Description
        Use this field to describe the exam's contents, what it assesses, and so on. This is shown in the exams index, so make sure it's fairly concise.

    Author's Notes
        Use this field to record notes for yourself or other authors about the design of the exam.

Navigation
==========

The navigation settings control how the student can move through the exam, and whether to give them warnings if they 

.. glossary::
    Allow user to regenerate questions?
        If ticked, then the "Try another question like this one" button is displayed at the bottom of each question, allowing the student to re-randomise the question and have another attempt at it.

    Allow move to previous question?
        If ticked, then the user is allowed to move back to a question after leaving it.

    Allow jump to any question?
        If ticked, then the user can jump between questions at will during the exam.

    Show front page?
        If ticked, then an intro screen is shown to the student before the exam starts, 

    On advance (event)
        What to do when the student moves to the next question.

    On reverse (event)
        What to do when the student moves to the previous question.

    On move (event)
        What to do when the student moves to any other question.


Timing
======

.. glossary::
    On timeout
        Display a message when the student runs out of time

    5 minutes before timeout
        Display a message five minutes before the student runs out of time

Feedback
========

.. glossary::
    Show actual mark?
        If ticked, the student will be shown their score for each question and part immediately after submitting their answers.
    Show total mark?
        If ticked, the student will be shown the maximum attainable score for each question and part.
    Show answer state?
        If ticked, then when the student submits an answer an icon will be displayed to let the student know if their answer was marked correct, partially correct or incorrect.
    Allow reveal answer?
        If ticked, then the "Reveal answer" button is enabled on each question. If the student chooses to reveal the answer to a question, they are shown the correct answer but lose all their marks and can not re-attempt the question.
    Advice threshold
        If the student's score is below this threshold, then the question advice is displayed.

Events
======

Some of the properties described above are marked as *events*. These all have the same structure: an *action* setting which determines how to react to the event, and a *message* to display to the student when appropriate.

Questions
=========

Select the questions to be included in the exam by searching for them in the box on the right-hand side and clicking the plus icon on questions you wish to use.

The order of questions can be rearranged by dragging and dropping questions using the up/down arrow handles on the left of each item.

Deleting a question from an exam does not remove it from the database. To permanently delete a question, click on its name and click the "Delete" button on the question's edit page.
