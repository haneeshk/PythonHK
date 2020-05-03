#!/usr/bin/env python
# coding: utf-8


from funcoperators import postfix as to, infix, compose as ov # composition operator
from numpy import *




@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func, [arg]))[0]
    return list(map(func, [arg]))[0]






if __name__ == '__main__':
    # test1.py executed as script
    # do something
    at()
