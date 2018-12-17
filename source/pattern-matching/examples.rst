.. _pattern-matching-examples:

Pattern-matching examples
=========================

The following examples demonstrate different features of the pattern-matching syntax, and particular behaviours that might not be immediately obvious.

Examples
--------

Get all :math:`x` terms in a polynomial::

    m_all(m_pm(m_all(??)*m_any(x,x^?)));xs+m_all(??);rest

Get the coefficient and degree of an :math:`x` term::

    m_pm(m_all(??);coefficient*m_any(x,x^?;degree))

Get both sides of an equation::

    ?;left=?;right

Check :math:`x` terms are collected on one side of an equation::

    m_uses(x);xside = m_not(m_uses(x));otherside

Check that a quadratic is factorised::

    (m_pm(??*x);a+?;b)*(m_pm(??*x);c+?;d)

Capture multiple powers of :math:`x` and :math:`y`::

    m_all( m_any( ??x, ??y, ??x^??, ??y^??, m_any(x,x^??)*m_any(y,y^??)*?? ) );terms + m_all(??;rest)
