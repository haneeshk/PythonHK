#!/usr/bin/env python
# coding: utf-8

from IPython.display import display as Echo
from numpy import *
from funcoperators import postfix as to, infix, compose as ov # composition operator


@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func, [arg]))[0]
    return list(map(func, [arg]))[0]




get_ipython().run_cell_magic('latex', '', '\n$$\\newcommand{\\u}[1]{\\boldsymbol{#1}}$$\n')
get_ipython().run_cell_magic('latex', '', '\n$$\\newcommand{\\usf}[1]{\\boldsymbol{\\mathsf{#1}}}$$\n')
