How do I...
==============


.. _include-an-image:

... include an image?
-----------------------

    It's best practice to attach images to questions so that they're distributed with the final compiled exam, rather than linking to images stored on a webserver. 

    When editing a content area, click on the :guilabel:`Insert/Edit Image` button. 
    You can then either pick an image you've already uploaded, or click the :guilabel:`Choose file` button to upload an image from your computer.

    You can resize images and add a title attribute by selecting the image in the content area and clicking on the :guilabel:`Insert/Edit Image` button.

    .. raw:: html

        <iframe src="https://player.vimeo.com/video/167083433" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>


.. _embed-a-video:

... embed a video?
------------------

    Upload your video to somewhere like YouTube or Vimeo. 
    Including videos in downloaded exam packages is a terrible idea, so we discourage that. 
    Click the :guilabel:`Embed image/video` button (it's a blue cloud), and paste in the URL of your video.

    .. raw:: html

        <iframe src="https://player.vimeo.com/video/167082427" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

.. _embed-a-diagram:

... include an interactive diagram?
-----------------------------------

    There are a couple of ways of including an interactive diagram in a Numbas question. 
    You can either embed a `GeoGebra <http://www.geogebra.org/>`_ applet, or use `JSXGraph <http://jsxgraph.uni-bayreuth.de/>`_.

    For JSXGraph diagrams, there is :ref:`an extension <jsxgraph-extension>` which takes care of most of the setup.

    GeoGebra applets can't communicate with the Numbas question and hence can't use randomised variables, but they can be used to illustrate questions in a generic way. 
    This screencast describes how to embed a GeoGebra applet in a Numbas question.

    .. raw:: html

        <iframe src="https://player.vimeo.com/video/167084424" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

.. _change-how-the-question-looks:

... change how the question looks?
----------------------------------

You can use the formatting tools in the question editor to style your text. 
However, if you repeat the same styles over and over, or want to change aspects of the layout such as space between elements or decoration, you'll need to write some CSS.

CSS is a language for defining how things should look - there's `a good introduction at Khan Academy <https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-css/>`_. 
In the Numbas editor, you can add CSS rules to a question in the :ref:`preamble` section.

The following questions demonstrate how to use CSS to change the look of a Numbas question:

* `Style a table of sales figures <https://numbas.mathcentre.ac.uk/question/2717/style-a-table-of-sales-figures/>`_ - 
* `Use CSS to style parallel translation <https://numbas.mathcentre.ac.uk/question/5599/use-css-to-style-parallel-translation/>`_ - CSS classes "english" and "cymraeg" apply different background colours to English and Welsh portions of text.
* `CSS Lemma environment <https://numbas.mathcentre.ac.uk/question/2704/css-lemma-environment/>`_ - defines a CSS class in the preamble which styles the "Lemma" environment, used in the statement.
* `More space between multiple choice answers <https://numbas.mathcentre.ac.uk/question/5307/more-space-between-multiple-choice-answers/>`_

.. _conditional-visibility:

... show one of several images based on a random variables?
-----------------------------------------------------------

See the question `Using a randomly chosen image <https://numbas.mathcentre.ac.uk/question/1132/using-a-randomly-chosen-image/>`_ for an example of one method.

... show one of several blocks of text based on a random variable?
------------------------------------------------------------------

Suppose you have a random variable ``a``, which has the value 1,2 or 3, corresponding to three different scenarios. 
First, write out the text for each scenario. 

.. image:: /_static/how_do_i/conditional_visibility.png

There is a button in the content editor labelled :guilabel:`Conditional visibility`. 
This allows you to give an expression (in :ref:`JME` syntax) which dictates whether or not the selected text is shown. 
For each scenario, select the corresponding text and click on the :guilabel:`Conditional visibility` button. 
Enter ``a=1`` for the first block, ``a=2`` for the second, and ``a=3`` for the third.

When you run the question, only the block of text corresponding to the value of ``a`` is shown.

You can see an example of this technique in the question `Conditional visibility <https://numbas.mathcentre.ac.uk/question/7711/conditional-visibility/>`_.

... make sure my generated variables satisfy a condition?
---------------------------------------------------------

Use the :ref:`variable testing <variable-testing>` tools.

... display a dollar sign?
--------------------------

Because the dollar symbol is used to delimit portions of LaTeX maths, you need to escape dollar signs intended for display by placing a backslash before them -- that is, write ``\$``. 
See `this example question <https://numbas.mathcentre.ac.uk/question/4528/displaying-a-dollar-sign/>`__.

... include a randomised LaTeX command?
---------------------------------------

If you want to include a LaTeX command in a string variable, remember that backslashes and curly braces in strings must be escaped. 
That means you should type two backslashes where you'd normally type one, and add a backslash before each left or right curly brace, for example ``\\frac\{1\}\{2\}`` produces the LaTeX ``\frac{1}{2}``.
You need to do this because the backslash is used as an escape character in strings so you can include quote marks, which would normally end the string. 
(For example, ``"he said \"hello\" to me"``)

If you substitute a string variable into a mathematical expression using ``\var``, it's normally assumed to represent plain text and displayed using the plain text font. 
If your string is really a partial LaTeX expression, you must mark it as such by wrapping it in ``latex()``, e.g. ``\var{latex(mystring)}``.

See `this example question <https://numbas.mathcentre.ac.uk/question/10342/displaying-a-randomised-latex-command/>`__.
