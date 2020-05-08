# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""

# %%

import re
import sympy

def genPatt(patt):
    """
    This is a temporary script file.
    """
    p=re.compile(str(patt))
    return lambda x: bool(re.search(p,str(x)))



# %%
_=2
_=genPatt("^s.*")
_=filter(_,dir(re))
print(list(_))

#%%

def only(patt,strs):
    _ = genPatt(patt)
    _ = filter(_, strs)
    return list(_)



def TableForm(lst):
    print(*lst, sep='\n')




#%%


import pprint
_=only("^s.*",dir(re))
print(_)
TableForm(_)

#%%
x=sympy.symbols('\mu')
