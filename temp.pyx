# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import re

def genPatt(patt):
    p=re.compile(str(patt))
    return lambda x: bool(re.search(p,str(x)))




_=2
print(_)
