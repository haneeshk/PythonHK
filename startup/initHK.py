#!/usr/bin/env python
# coding: utf-8


from funcoperators import postfix as to, infix, compose as ov # composition operator


@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func, [arg]))[0]
    return list(map(func, [arg]))[0]
