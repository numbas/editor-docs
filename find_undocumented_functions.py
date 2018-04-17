"""
Find JME functions which have not been documented yet.
Set RUNTIME_DIR to the path of your Numbas runtime repository
"""

import re
import os

RUNTIME_DIR = '../dev'

with open('source/jme-reference.rst') as f:
    jme_docs = f.read()
documented_fns = [m.group(1) for m in re.finditer(r'function:: ([a-z_]+?)(\(|$)',jme_docs,flags=re.M)]
documented_fns.sort()

with open(os.path.join(RUNTIME_DIR,'runtime/scripts/jme-builtins.js')) as f:
    jme_builtins = f.read()
defined_fns = sorted(set([m.group(1) for m in re.finditer(r'newBuiltin\(\'([a-z_]+?)\'',jme_builtins)]))

undocumented = [f for f in defined_fns if f not in documented_fns and not re.search(r'function:: .*'+f,jme_docs)]

if len(undocumented):
    print("The following functions have not been documented:")
    for f in undocumented:
        print(f)
else:
    print("Every function has been documented")
