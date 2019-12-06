#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()
    
    #pythonmodules.run("setup.py build_sphinx")
    
def check():
    pythonmodules.compile("test")

def install():
    pythonmodules.install()