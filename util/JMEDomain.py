import re

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, TypedField


jme_sig_re = re.compile(
    r'''^ ((?:\$?[a-zA-Z_][a-zA-Z0-9_]*'*)|\?|[π∞])               # thing name
          (?: \((.*)\)                  # optional: arguments
          )? $                          # and nothing more
          ''', re.VERBOSE)


def _pseudo_parse_arglist(signode, arglist):
    """"Parse" a list of arguments separated by commas.

    Arguments can have "optional" annotations given by enclosing them in
    brackets.  Currently, this will split at any comma, even if it's inside a
    string literal (e.g. default argument value).
    """
    paramlist = addnodes.desc_parameterlist()
    stack = [paramlist]
    try:
        for argument in arglist.split(','):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith('['):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith(']'):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith(']'):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith('['):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += addnodes.desc_parameter(argument, argument)
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated paramlist node
        signode += addnodes.desc_parameterlist()
        signode[-1] += addnodes.desc_parameter(arglist, arglist)
    else:
        signode += paramlist


class JMEObject(ObjectDescription):
    option_spec = {
    }

    doc_field_types = [
        TypedField('parameter', label=l_('Parameters'),
                   names=('param', 'parameter', 'arg', 'argument'),
                   typerolename='obj', typenames=('paramtype', 'type'),
                   can_collapse=True),
        Field('returnvalue', label=l_('Returns'), has_arg=False,
              names=('returns', 'return')),
        Field('returntype', label=l_('Return type'), has_arg=False,
              names=('rtype',)),
    ]

    def get_signature_prefix(self, sig):
        """May return a prefix to put before the object name in the
        signature.
        """
        return ''

    def needs_arglist(self):
        """May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return True

    def handle_signature(self, sig, signode):
        """Transform a JME signature into RST nodes.

        Return (fully qualified name of the thing, classname if any).
        """
        m = jme_sig_re.match(sig)
        if m is None:
            raise ValueError
        name, arglist = m.groups()

        fullname = name

        signode['fullname'] = fullname

        signode += addnodes.desc_name(name, name)
        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += addnodes.desc_parameterlist()
            return fullname, ''

        _pseudo_parse_arglist(signode, arglist)
        return fullname, ''

    def get_index_text(self, name):
        """Return the text for the index entry of the object."""
        raise NotImplementedError('must be implemented in subclasses')

    def add_target_and_index(self, name_cls, sig, signode):
        fullname = name_cls[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['jme']['objects']
            if fullname in objects:
                self.state_machine.reporter.warning(
                    'duplicate object description of %s, ' % fullname +
                    'other instance in ' +
                    self.env.doc2path(objects[fullname][0]) +
                    ', use :noindex: for one of them',
                    line=self.lineno)
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(name_cls)
        if indextext:
            self.indexnode['entries'].append(('single', indextext, fullname, False, ''))

class JMEFunction(JMEObject):
    """
    Description of a JME function
    """

    def needs_arglist(self):
        return True

    def get_index_text(self, name_cls):
        return name_cls[0]

class JMEData(JMEObject):
    """
    Description of a JME data element (type, variable or constant)
    """

    def needs_arglist(self):
        return False

    def get_index_text(self, name_cls):
        return name_cls[0]

    def handle_signature(self, sig, signode):
        """Transform a JME signature into RST nodes.

        Return (fully qualified name of the thing, classname if any).
        """
        m = jme_sig_re.match(sig)
        if m is None:
            raise ValueError
        name, _ = m.groups()
        signode['fullname'] = name
        signode += addnodes.desc_name(name, name)
        return name, ''

class JMEXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        return title, target


class JMEDomain(Domain):
    """JME domain."""
    name = 'jme'
    label = 'JME'
    object_types = {
        'function': ObjType(l_('function'), 'func', 'obj'),
        'data': ObjType(l_('data'), 'data', 'obj'),
        'variable': ObjType(l_('variable'), 'var', 'obj'),
    }

    directives = {
        'function': JMEFunction,
        'data': JMEData,
        'variable': JMEData,
    }
    roles = {
        'func':  JMEXRefRole(fix_parens=True),
        'data':  JMEXRefRole(),
        'var': JMEXRefRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
    }

    def clear_doc(self, docname):
        for fullname, (fn, _) in list(self.data['objects'].items()):
            if fn == docname:
                del self.data['objects'][fullname]

    def find_obj(self, name):
        objects = self.data['objects']
        if name in objects:
            return [(name,objects[name])]
        else:
            return []

    def resolve_xref(self, env, fromdocname, builder,
                     type, target, node, contnode):
        matches = self.find_obj(target)
        if not matches:
            return None
        elif len(matches) > 1:
            env.warn_node(
                'more than one target found for cross-reference '
                '%r: %s' % (target, ', '.join(match[0] for match in matches)),
                node)
        name, obj = matches[0]

        return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def get_objects(self):
        for refname, (docname, type) in self.data['objects'].items():
            yield (refname, refname, type, docname, refname, 1)

def setup(app):
    app.add_domain(JMEDomain)
