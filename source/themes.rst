Themes
======

A Numbas theme is a package of files containing everything needed to display an exam in the browser. This includes an HTML file, CSS stylesheets, and JavaScript to manage coordination between the page and the exam runtime.

Contents of a theme
-------------------

A theme is a folder containing the following three things:

* A ``files`` folder containing files to be included in the compiled exam. At the minimum, this contains a file ``index.html`` and a JavaScript file ``display.js``.
* An ``xslt`` folder containing a file ``question.xslt`` to be used when generating the HTML to accompany questions.
* An optional file called ``inherit.txt`` containing the name of a theme to extend.

JavaScript and CSS files
************************

All JavaScript and CSS files used by a Numbas exam are collected into two files, ``scripts.js`` and ``styles.css``. These are the only files you need to load from your theme's ``index.html`` - all script and stylesheet files, including those provided by your theme, are collected into these.

Building off an existing theme
------------------------------

At the top of your theme folder, place a file called ``inherit.txt`` containing the name of the theme to extend, e.g. `default`. When an exam is compiled using your theme, all of the parent theme's files will be included, and then all of the files belonging to your theme, overriding any files of the same name from the parent theme.
