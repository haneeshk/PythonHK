import numpy as np
from functional_notations import _F as _f, F as f


sin=_f(np.sin)
sin@(np.pi)
sin(np.pi)


mult1@2
f@np.sin@(np.pi/2)

list([1,2])
f@list@([np.pi/4, 2.0])


print=_f(print)
print([1,2,3])
print@[1,2,3]
f@list([np.pi/4])

from multimethod import  multimethod, overload, isa



@multimethod
def fun(x: int):
        return x+1

@multimethod
def fun(x: float):
        return x+2


if(x>3,True,)

@overload
def fun1(x:  lambda x: x>3):
        return x+3.0


@overload
def fun1(x:  (isa(tuple) and (lambda x : x[0]>3))):
        return x


@overload
def fun1(x:  (isa(list) and (lambda x : x[0]>3))):
        return x

(4.0,3.0)[0]
y=f@tuple@[4.0,3.0];
y
x=fun1(y)


f@print@[id(y),type(y),id(x),type(x)]


x[0]=0.0
y

f@print@[id(y),type(y),id(x),type(x)]



names=['John', 'James','Bill']
f@list@map(lambda x: x+' smith',names)
lase
