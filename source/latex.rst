.. _LaTeX notation:

LaTeX notation
==============

LaTeX is the de facto standard mark-up language for mathematical notation. It's syntactically very simple, but there's a fairly steep learning curve in learning the names of commands.

In Numbas, **inline maths** (maths notation that sits on the same line as the surrounding text) is delimited either by dollar signs, e.g.::

    Calculate the expansion up to the $x^4$ term.

produces

    Calculate the expansion up to the :math:`x^4` term.

**Display-mode** maths, which is displayed on its own line and rendered less compactly, is delimited by ``\[`` and ``\]``. For example::

    The quadratic formula is \[ x = \frac{ -b \pm \sqrt{ b^2-4ac } }{ 2a } \]

produces

    The quadratic formula is 
    
    .. math::

        x = \frac{ -b \pm \sqrt{ b^2-4ac } }{ 2a }
    
If you've never used LaTeX before, a couple of good places to start are the `LaTeX maths Wikibook <http://en.wikibooks.org/wiki/LaTeX/Mathematics>`_ and the `Art of Problem Solving LaTeX Guide <http://www.artofproblemsolving.com/Wiki/index.php/LaTeX:Commands>`_. Bear in mind that LaTeX is only used for maths-mode, so the text-mode LaTeX commands don't apply.

To find the command for a symbol you want to use, draw it in `Detexify <http://detexify.kirelabs.org/classify.html>`_ and it will show you the commands for the most similar-looking symbols.
