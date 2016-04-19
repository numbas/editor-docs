Themes
======

A Numbas theme is a package of files containing everything needed to display an exam in the browser. This includes an HTML file, CSS stylesheets, and JavaScript to manage coordination between the page and the exam runtime.

Contents of a theme
-------------------

A theme is a folder containing the following three things:

* An optional file called ``inherit.txt`` containing the name of a theme to extend.
* A folder called ``files`` containing files to be included in the compiled exam. For a theme which does not extend another, this contains at the minimum a file ``index.html`` and a JavaScript file ``display.js``.
* A folder called ``xslt`` containing a file ``question.xslt`` to be used when generating the HTML to accompany questions.

JavaScript and CSS files
************************

All JavaScript and CSS files used by a Numbas exam are collected into two files, ``scripts.js`` and ``styles.css``. These are the only files you need to load from your theme's ``index.html`` - all script and stylesheet files, including those provided by your theme, are collected into these.

Building off an existing theme
------------------------------

At the top of your theme folder, place a file called ``inherit.txt`` containing the name of the theme to extend, e.g. `default`. 
When an exam is compiled using your theme, all of the parent theme's files will be included, and then all of the files belonging to your theme, overriding any files of the same name from the parent theme.

The default theme is packaged with the Numbas compiler; if you want to modify it you should first download the Numbas repository from https://github.com/numbas/Numbas and copy the folder ``themes/default``.

Uploading a theme to the editor
-------------------------------

Package your theme's files into a .zip file. Next, go to the Numbas editor and click on the :guilabel:`Your profile` link, then :guilabel:`Your themes`. The :guilabel:`Upload a new theme` takes you to a form where you can upload the .zip file you created, and give it a human-readable name. You will be able to select any of your themes in the exam edit page.

If you make changes to your theme, go back to the :guilabel:`Your themes` page and click on the :guilabel:`Edit` link, then upload a revised .zip file.

This screencast gives a quick summary of a theme package's contents, then shows how to create a theme which replaces the Numbas logo.

.. raw:: html
    
    <div style="text-align: center;"><iframe src="http://player.vimeo.com/video/105023576" width="600" height="337" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

Examples
********

* Replace the Numbas logo: :download:`change-logo-theme.zip <_static/themes/change-logo-theme.zip>`
* Add custom CSS rules: :download:`extra-css-theme.zip <_static/themes/extra-css-theme.zip>`
