MatConstants=(("Young's Modulus",13.3,"KPa"),("pi",3.14,"Non-dimensional"))
MatConstantsKeys=( (i,entry[0]) for i,entry in enumerate(MatConstants))
MatConstantsKeys
MatConstantsKeys=tuple(MatConstantsKeys)
MatConstantsKeys


class YoungsModulus():
    __value__
    __units__
    def __init__(self,value,units="KPa"):
        __value__=value
        __units__=units




from IPython.display import display as Echo
from numpy import *
import numpy as np
from funcoperators import postfix as to, infix, compose as ov # composition operator
@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func,[arg]))[0]
