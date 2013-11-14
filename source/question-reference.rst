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

.. _statement:

Statement
=========

The statement is a :ref:`content-area` which appears at the top of the question, before any input boxes. Use the statement to set the question and provide any information the student needs to answer it.


Variables
=========

Variables are defined using :doc:`jme-reference` syntax. 

The :guilabel:`Computed value` column shows a generated value for each variable. Note that when the question is delivered to students, the variable values are generated with each new attempt, so students won't necessarily see the same values as those displayed here. It's a good idea to use the :guilabel:`Regenerate values` button a few times to check that randomised variables don't take unsuitable values.

You can reorder the variables in the list by dragging the arrow icons. Doing this doesn't affect the way values are computed.

This screencast gives a quick summary of how the variable editing interface works:

.. raw:: html
    
    <div style="text-align: center;"><iframe src="http://player.vimeo.com/video/59575797" width="600" height="337" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

This screencast describes which variable names are valid, and gives some advice on how you should pick names:

.. raw:: html
    
    <div style="text-align: center;"><iframe src="http://player.vimeo.com/video/59577617" width="600" height="337" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>


Functions & Rulesets
====================

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

    .. _rulesets:

JME functions
-------------

Functions defined using JME work similarly to variables - the function's parameters are substituted into the expression, which is then evaluated.

Comments can be added to function definitions in the same way as variable definitions - anything on a line after two forward slashes is interpreted as a comment and not evaluated. For example::

    map(
        log(n),    //take log of n
        n,         //for n in
        1..10      //the range 1 to 10 (inclusive)
    )

JME does not allow for much control over program flow. Most importantly, there are no loops. Some functions can naturally be defined recursively, but note that recursive function calls can be very slow, since recursion isn't optimised.

Here's an example of a function which computes the :math:`n`\ :sup:`th` Fibonacci number recursively::

    //nth fibonacci number
    //f(0) = f(1) = 1
    //f(n+2) = f(n)+f(n+1)
    if(n<=1,
        1,
    //else
        f(n-2)+f(n-1)
    )

Javascript functions
--------------------

Writing a function in Javascript allows you to use all of that language's features, such as loops, anonymous functions and DOM manipulation. Functions defined in Javasript don't need the ``function(parameters) { ... }`` enclosure - that's provided by Numbas - but they do need to return a value.

Numbas provides a large library of functions which you can use. These are accessed from the objects ``Numbas.math`` and ``Numbas.util``. The best way to see what's available is to look at the Numbas source code - `math.js <https://github.com/numbas/Numbas/blob/master/runtime/scripts/math.js>`_; `util.js <https://github.com/numbas/Numbas/blob/master/runtime/scripts/util.js>`_. jQuery is also available. 

While the JME system has its own type system for variables, separate from Javascript's, function parameters are unwrapped to native Javascript values on evaluation so you normally don't need to worry about it.

.. topic:: Examples

    .. highlight:: javascript

    This function takes a list of strings and returns an HTML bullet list::
        
        var ol = $('<ol>');  // create list element

        for(var i=0; i<things.length; i++) {
            ol.append($('<li>').html(things[i]));	//append list item to list
        }
          
        return ol;	//return list

    This function creates an HTML5 ``canvas`` element and draws a rectangle with the given dimensions, along with labels::

        var c = document.createElement('canvas');
        $(c).attr('width',w+40).attr('height',h+40);
        var context = c.getContext('2d');

        //fill in rectangle with a light shade
        context.fillStyle = '#eee';
        context.fillRect(5,5,w,h);

        //draw outline
        context.strokeStyle = '#000';
        context.lineWidth = 3;
        context.strokeRect(5,5,w,h);

        //draw labels
        context.fillStyle = '#000';
        context.font = '20px sans-serif';
        var wstring = w+'m';
        var tw = context.measureText(wstring).width;
        context.fillText(wstring,5+(w-tw)/2,5+h+25);

        var hstring = h+'m';
        var hw = context.measureText(hstring).width;
        context.save();
        context.translate(5+w+25,5+(h+hw)/2);
        context.rotate(-Math.PI/2);
        context.fillText(hstring,0,0);

        return c;

    You can see this function in use at https://numbas.mathcentre.ac.uk/question/759/use-canvas-to-draw-a-rectangle/.

    This function formats a number with commas to separate every third digit, i.e. :math:`1,\!000,\!000` instead of :math:`1000000`::

        var parts=n.toString().split(".");
        if(parts[1] && parts[1].length<2) {
          parts[1]+='0';
        }
        return parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",") + (parts[1] ? "." + parts[1] : "");

    You can see this function in use at https://numbas.mathcentre.ac.uk/question/396/numerical-reasoning-average-salary/.

Rulesets
--------

A "ruleset" defines a list of named :doc:`simplification rules <simplification>` used to manipulate mathematical expressions.

Parts
=====

See the page on :ref:`question-parts`.


.. _advice:

Advice
======

:guilabel:`Advice` is a :ref:`content-area` which is shown when the student presses the :guilabel:`Reveal` button to reveal the question's answers, or when they receive less than the exam's :term:`Advice threshold` after submitting their answers.

The advice area is normally used to present a worked solution to the question.

Exams using this question
=========================

A list of links to each of the exams which contain this question, for convenience.

Access
======

You can control who is allowed to see, and edit, your questions.

.. topic:: Public visibility

    .. glossary::
        Hidden
            Only you and users named in the :guilabel:`Individual access rights` section can see this question.

        Anyone can see this
            Anyone, even users who are not logged in, can see this question. Only you and users named in the :guilabel:`Individual access rights` section can edit this question.

        Anyone can edit this
            Anyone, even users who are not logged in, can see and edit this question.

.. topic:: Individual access rights

    Type a name into the search box to find a user. Click on a user's name in the results list to add them to the access list. Named users can have the following rights:

    .. glossary::
        Can view this
            The named user can see, but not edit, this question.

        Can edit this
            The named user can see this question and make changes to it.

