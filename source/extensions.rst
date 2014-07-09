Extensions
==========

Creating an extension
--------------------

An extension is a folder containing one or more files that should be included in an exam. They can be javascript files, CSS stylesheets, or any other kind of resource. By default, the Numbas compiler will look for extensions in its :file:`extensions` subdirectory.

The minimum an extension must contain is a file named `<extension-name>.js`, containing the following::

    Numbas.queueScript('extensions/extension-name/extension-name.js',['base'],function() {

    });

This wrapper tells Numbas that the extension has loaded. Because Numbas can't guarantee the order script files will be loaded in, code which uses the `Numbas` object must be placed inside this wrapper.

Using an extension with the editor
----------------------------------

To make an extension available in the editor, use the admin page to add a new :guilabel:`Extension` object. The :guilabel:`location` field is the path to the extension's folder, relative to the Numbas compiler's :file:`extensions` subdirectory. Once you've added the extension through the admin interface, you must also copy :file:`extension-name/extension-name.js` to :file:`{STATIC_ROOT}/js/numbas/extensions/extension-name/extension-name.js` so that any commands it provides can be used in the question editor.

Adding JME functions
--------------------

An extension can add JME functions (or rulesets, or anything else that goes in a `Scope <http://numbas.github.io/Numbas/Numbas.jme.Scope.html>`_ object by defining ``Numbas.extensions.<extension-name>.scope``. Here's an example which adds a single JME function::

    Numbas.queueScript('extensions/myExtension/myExtension.js',['jme'],function() {
        var myExtension = Numbas.extensions.myExtension = {};
        var extensionScope = myExtension.scope = new Numbas.jme.Scope();

        var funcObj = Numbas.jme.funcObj;
        var TNum = Numbas.jme.types.TNum;

        extensionScope.addFunction(new funcObj('difference',[TNum,TNum],TNum,function(a,b){ return Math.abs(a-b); }, {unwrapValues:true}));
    })


First-party extensions
----------------------

.. toctree::
    :maxdepth: 1

    extensions/jsxgraph
    extensions/stats

