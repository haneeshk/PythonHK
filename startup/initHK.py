#!/usr/bin/env python
# coding: utf-8





# %codecell
from funcoperators import postfix as to, infix, compose as ov # composition operator
from numpy import *



@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func, [arg]))[0]
    return list(map(func, [arg]))[0]



from functional_notations import _F as _f, F as f
# for demo see Demos/functional_notation_demo.py


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    at()
