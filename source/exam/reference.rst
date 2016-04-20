Exams
*****

An exam is a collection of questions which you will give to your students. 
Within an exam you can set a pass mark, as well as configure how much feedback students can receive and how they can navigate between questions.

For a quick introduction to the workflow involved in putting an exam together, see the :doc:`tutorial on creating an exam </tutorials/create-exam>`.

The exam editor
===============

At the top of the exam editor is the exam's name, as well as any feedback stamp which has been attached. 
On the left of the screen are :ref:`exam-admin-controls` and labels for each of the editing tabs.

.. _exam-admin-controls:

Admin controls
==============

.. todo:: Pic of admin buttons

.. glossary::
    Test Run
        Opens a preview of the exam in a new window.

        .. warning:: 
            Do **NOT** use this link to deliver the exam to students. 
            This link is not permanent and could stop working at any time.
            Instead, download the exam and put it either on your own webspace or in a VLE.

    Feedback
        Use this button to give feedback about the quality of an exam, after test running it. 
        The options are listed in descending order of "suitability for use":

        * **Ready to use** - this exam is of sufficient quality to give to students.
        * **Should not be used** - this exam works, but you deprecate its use - for example, if it's not intended for use by students, or there's a better version elsewhere.
        * **Has some problems** - this exam works, but has some problems which mean it's not ready for use by students - for example, the exam is incomplete, or changes need to be made to the text. 
          Further work is needed before this exam can be given to students.
        * **Doesn't work** - this exam doesn't even run!
        * **Needs to be tested** - this exam looks alright to me, but it should be checked thoroughly before being used.

    Download
        Links to download standalone packages of the exam. 

        * **SCORM package** - a compiled package of the exam with SCORM files included, so it can be uploaded to a VLE and communicate with its gradebook.
        * **standalone .zip** - a compiled package of the exam, ready to run anywhere without connecting to a VLE. 
        * **source** - a plain-text representation of the exam, to be used with the Numbas command-line tools or as a backup.

Settings
========

The settings tab is where you set up metadata describing the exam.

Try to make sure not to ignore the settings tab, even if you just want to get a working exam as quickly as possible - a good name and description will make it much easier to find your exam again in the future!

.. glossary::
    Name
        This is shown to the student and used for searching within the editor, so make it something intelligible. 
        "Linear algebra diagnostic test" is a good name; "L.A. t1 v1" is not.

    Description
        Use this field to describe the exam's contents, what it assesses, and so on. 
        This is shown in the exams index, so make sure it's fairly concise.

    Tags
        Use tags to categorise exams so they can be found through the search function. 
        Your guiding principle should be "more is better" - try to write down all words that someone searching for this exam might use.

        After typing a tag in the box, press the :kbd:`Enter` key to add it to the list.

    Licence
        You can specify the licence under which you are making your resources available. 
        Different licences allow other users to copy, modify or reuse your content in different ways - consider which licence to choose carefully. 
        *CC BY* allows other users to reuse your content however you like, as long as they give appropriate credit to you.

    Pass threshold
        Define a pass/fail threshold for the exam. 
        The pass/fail message will be displayed when the student ends the exam. 
        If set to zero, then no message is displayed.

    Delete
        Delete the exam permanently from the database. 
        The associated questions are not deleted - you must delete them individually, if you want them to be deleted too.

    Make a Copy
        Create a copy of the exam. 
        Use this to make changes to an exam which does not belong to you.

Display
=======

.. glossary::

    Interface theme
        Themes control the user interface of an exam, changing the look and feel. 
        The `default` theme is designed for exams which will be delivered over the web. 
        There is also a `worksheet` theme which can be used to print out multiple, randomised copies of an exam for students to complete on paper.

    Interface language
        Specify which translation to use for the text in the user interface, i.e. button labels, error messages, etc.

Questions
=========

Select the questions you want to include in your exam on this tab.
You can use every question selected, or pick a random subset each time the exam is started.

.. glossary::

    Shuffle questions?
        If ticked, then the questions will be shown to the student in a random order. 
        The order is randomised on each attempt.

    Use all questions?
        This option is only visible if :term:`Shuffle questions?` is ticked.
        If ticked, then every question in the list will be shown to the student. 
        If not, then only the number specified below will be used.

    Number of questions to display
        The number of questions to show to the student.

    Pass threshold
        The percentage score the student must obtain over all questions to pass the exam.
        If this is set to 0, then the student will not be shown a pass/fail message.

The tabs on the right hand side offer different ways of finding questions to add to the exam.

* The :guilabel:`Basket` tab shows questions you've added to your basket: you can browse the question editor to find questions, add them to your basket, and then go back to the exam editing page and add them in.
* The :guilabel:`Recent questions` tab shows questions you have recently edited.

You can check a question does what you want and give it a test run before including it in your exam: click on the question's name to open its editing page in a new window.

Click the plus icon on one of the question results to add it to your exam. 

.. image:: images/exam_edit_add_question.png

You can drag and drop questions in the list on the left to reorder them.

.. image:: images/exam_edit_drag.png

The :guilabel:`Replace this question with a copy` lets you quickly swap in a duplicate of a question you've included in your exam. 
If you're using a question created by someone else, this is a convenient way of getting a version of the question you can make changes to.

.. note:: 

    Deleting a question from an exam does not remove it from the database. 
    To permanently delete a question, click on its name and click the :guilabel:`Delete` button on the question's edit page.

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

    Show results page?
        If ticked, then the student is shown a page summarising the results of their exam after finishing. 
        If this is not ticked, then the exam exits as soon as the student finishes, and they get no immediate feedback about their scores.

    Confirm before leaving the exam while it's running?
        If ticked, the student will be asked to confirm that they really want to leave if they try to close the exam while it's running, for example by pressing the browser's back button or closing the tab the exam is running in.

    On leaving a question
        What to do when the student changes question, or tries to end the exam. 
        You can either warn the student and make them confirm that they'd like to leave, or prevent them from leaving the question entirely until they've answered it.

Timing
======

.. glossary::
    Exam duration
        The length of time students are allowed to attempt the exam. 
        If set to zero, then there is no time limit.

    Allow pausing?
        If ticked, the student can pause the exam while running it, and the timer will stop. 
        If unticked, there is no pause button, and the end time is fixed when the session starts - leaving and resuming through the VLE will not affect the end time.

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
        If ticked, then the :guilabel:`Reveal answer` button is enabled on each question. 
        If the student chooses to reveal the answer to a question, they are shown the correct answer but lose all their marks and can not re-attempt the question.

    Advice threshold
        If the student's score is below this threshold, then the question advice is displayed.

Events
======

Some of the properties described above are marked as *events*. 
These all have the same structure: an :guilabel:`action` setting which determines how to react to the event, and a :guilabel:`message` to display to the student when appropriate.

Editing history
===============

Each time you make a change to a exam, it's saved to the database. 
You can see the full editing history of your exam in this tab, and revert back to a previous state by clicking on the :guilabel:`Restore` link.

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
            Anyone, even users who are not logged in, can see this exam. 
            Only you and users named in the :guilabel:`Individual access rights` section can edit this exam.

        Anyone can edit this
            Anyone, even users who are not logged in, can see and edit this exam.

.. topic:: Individual access rights

    Type a name into the search box to find a user. 
    Click on a user's name in the results list to add them to the access list. 
    Named users can have the following rights:

    .. glossary::

        Can view this
            The named user can see, but not edit, this exam.

        Can edit this
            The named user can see this exam and make changes to it.

.. topic:: Access links
    
    The URLs in this section automatically grant access to whoever follows them. 
    You could use these links to share a question with someone who hasn't yet created an account on the editor, or to share a question with a group of people without inviting each person individually.

    .. warning::
        These URLs grant access to whoever clicks on them, so be careful about how they're shared.
