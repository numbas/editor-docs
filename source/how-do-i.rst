How do I...
==============

.. _include-an-image:

... include an image?
-----------------------

    It's best practice to attach images to questions so that they're distributed with the final compiled exam, rather than linking to images stored on a webserver. 

    When editing a :ref:`content-area`, click on the :guilabel:`Insert/Edit Image` button. You can then either pick an image you've already uploaded, or click the :term:`Choose file` button to upload an image from your computer.

    You can resize images and add a title attribute by selecting the image in the :ref:`content-area` and clicking on the :guilabel:`Insert/Edit Image` button.

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

See the question `Show a block of HTML based on a random value <https://numbas.mathcentre.ac.uk/question/1191/show-a-block-of-html-based-on-a-random-value/>`_ for an example of one method.
