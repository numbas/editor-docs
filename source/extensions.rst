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

Adding a new JME data type
--------------------------

JME data types are JavaScript objects, distinguished by their ``type`` property. The object should have a `value` property which contains the data it represents. The JME system can happily use new data types, but you'll need to tell it how to render them as LaTeX or JME code. This is done by adding methods to ``Numbas.jme.display.typeToTeX`` and ``Numbas.jme.display.typeToJME``. Once you've defined how to create and display the new data type, you can add functions dealing with it in the same way as for the built-in data types.

Here's an example extension which defines a toy "chemical" data type (excuse the bad chemistry)::

    Numbas.queueScript('extensions/chemicals/chemicals.js',['jme','jme-display'],function() {

        // set up the extension's scope
        var chemicals = Numbas.extensions.chemicals = {};
        var chemicalsScope = chemicals.scope = new Numbas.jme.Scope();

        // Define the constructor for a new data type representing a chemical formula
        // `formula` is a dictionary mapping element symbols to the number of atoms present
        function TChemical(formula) {
            this.value = formula;
        }
        TChemical.prototype.type = 'chemical';

        // define a couple of example formulas
        chemicalsScope.variables.oxygen = new TChemical({O:2});
        chemicalsScope.variables.water = new TChemical({H:2, O:1});

        // Code to render a chemical formula as LaTeX
        Numbas.jme.display.typeToTeX.chemical = function(thing,tok,texArgs,settings) {
            var out = '';
            for(var element in tok.value){ 
                out += element;
                var num = tok.value[element];
                if(num>1) {
                    out += '_{'+num+'}';
                }
            }
            return '\\mathrm{'+out+'}';
        }

        // Code to render a chemical formula as a JME expression
        Numbas.jme.display.typeToJME.chemical = function(tree,tok,bits,settings) {
            var out = '';
            for(var element in tok.value) {
                if(out.length) {
                    out += '+';
                }
                out += 'molecule("'+element+'",'+tok.value[element]+')'
            }
            return out;
        }

        var funcObj = Numbas.jme.funcObj;
        var TString = Numbas.jme.types.TString;
        var TNum = Numbas.jme.types.TNum;

        // define addition on chemicals: add up the elements in each formula
        chemicalsScope.addFunction(new funcObj('+',[TChemical,TChemical],TChemical,function(c1,c2) {
            var nformula = {};
            var element;
            for(element in c1) {
                nformula[element] = c1[element];
            }
            for(element in c2) {
                if(element in nformula) {
                    nformula[element] += c2[element];
                } else {
                    nformula[element] = c2[element];
                }
            }
            return nformula;
        }));

        // define a function to create a molecule with given number of atoms of given element
        chemicalsScope.addFunction(new funcObj('molecule',[TString,TNum],TChemical,function(element,numatoms) {
            var formula = {};
            formula[element] = numatoms;
            return formula;
        }));

        // define a JME functions which tells you how many of the given element are in a formula
        chemicalsScope.addFunction(new funcObj('numatoms',[TChemical,Numbas.jme.types.TString],Numbas.jme.types.TNum,function(chemical,element) {
            if(element in chemical) {
                return chemical[element];
            } else {
                return 0;
            }
        }));
    });


First-party extensions
----------------------

.. toctree::
    :maxdepth: 1

    extensions/jsxgraph
    extensions/stats

