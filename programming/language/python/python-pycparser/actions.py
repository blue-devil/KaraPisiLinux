#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()
    
def check():
    pythonmodules.run("tests/all_tests.py")

def install():
    pythonmodules.install()

    for dirs in ["examples"]:
        pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), dirs)
