MatConstants=(("Young's Modulus",13.3,"KPa"),("pi",3.14,"Non-dimensional"))
MatConstantsKeys=( (i,entry[0]) for i,entry in enumerate(MatConstants))
MatConstantsKeys
MatConstantsKeys=tuple(MatConstantsKeys)
MatConstantsKeys


class YoungsModulus():
    __value__=0.0
    __units__="KPa"
    def __init__(self,value,units=__units__):
        self.__value__=value
        self.__units__=units
    def value(self):
        return self.__value__


YM=YoungsModulus(10,"MPa")
YM2=YoungsModulus(10)

def CreateConstant(Value,Unit="ND"):
    return lambda x=0 :  Unit if x is "units" else Value

ν=CreateConstant(0.3)
E=CreateConstant(220,"KPa")
ν()
ν("units")
ν("units")

ν("Value")*E("Value")
E("value")


E=22.0

E()=33


def YM(x : str):
    if x is "value":
        return 22.0
    elif x is "units":
        return "KPa"
    return "0"

YM("value")


wYM2.__units__
from IPython.display import display as Echo
from numpy import *
import numpy as np
from funcoperators import postfix as to, infix, compose as ov # composition operator
@infix
def at(func, arg):                          # evaluate at operator
    return list(map(func,[arg]))[0]
