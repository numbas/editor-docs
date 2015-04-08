How do I...
==============

.. _include-an-image:

... include an image?
-----------------------

    It's best practice to attach images to questions so that they're distributed with the final compiled exam, rather than linking to images stored on a webserver. 

    When editing a content area, click on the :guilabel:`Insert/Edit Image` button. You can then either pick an image you've already uploaded, or click the :guilabel:`Choose file` button to upload an image from your computer.

    You can resize images and add a title attribute by selecting the image in the content area and clicking on the :guilabel:`Insert/Edit Image` button.

    .. raw:: html

        <iframe src="http://player.vimeo.com/video/65654893" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>


.. _embed-a-video:

... embed a video?
------------------

    Upload your video to somewhere like YouTube or Vimeo. Including videos in downloaded exam packages is a terrible idea, so we discourage that. Click the :guilabel:`Embed image/video` button (it's a blue cloud), and paste in the URL of your video.

    .. raw:: html

        <iframe src="http://player.vimeo.com/video/58530295" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

.. _embed-a-diagram:

... include an interactive diagram?
-----------------------------------

    There are a couple of ways of including an interactive diagram in a Numbas question. You can either embed a `GeoGebra <http://www.geogebra.org/>`_ applet, or use `JSXGraph <http://jsxgraph.uni-bayreuth.de/>`_.

    For JSXGraph diagrams, there is :ref:`an extension <jsxgraph-extension>` which takes care of most of the setup.

    GeoGebra applets can't communicate with the Numbas question and hence can't use randomised variables, but they can be used to illustrate questions in a generic way. This screencast describes how to embed a GeoGebra applet in a Numbas question.

    .. raw:: html

        <iframe src="http://player.vimeo.com/video/80277201" width="500" height="281" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

    The question `GeoGebra demo <https://numbas.mathcentre.ac.uk/question/2207/geogebra-demo/>`_ contains examples of of GeoGebra applets embedded as standalone resources, and through `GeoGebraTube <http://www.geogebratube.org/>`_.

... show one of several images based on a random variables?
-----------------------------------------------------------

See the question `Using a randomly chosen image <https://numbas.mathcentre.ac.uk/question/1132/using-a-randomly-chosen-image/>`_ for an example of one method.

... show one of several blocks of text based on a random variable?
------------------------------------------------------------------

Suppose you have a random variable ``a``, which has the value 1,2 or 3, corresponding to three different scenarios. First, write out the text for each scenario. 

.. image:: _static/images/screenshots/conditional_visibility.png

There is a button in the content editor labelled :guilabel:`Conditional visibility`. This allows you to give an expression (in :ref:`JME` syntax) which dictates whether or not the selected text is shown. For each scenario, select the corresponding text and click on the :guilabel:`Conditional visibility` button. Enter ``a=1`` for the first block, ``a==2`` for the second, and ``a=3`` for the third.

When you run the question, only the block of text corresponding to the value of ``a`` is shown.

You can see an example of this technique in the question `Conditional visibility <https://numbas.mathcentre.ac.uk/question/7711/conditional-visibility/>`_.
