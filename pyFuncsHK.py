import re
def genPatt(patt):
    p=re.compile(str(patt))
    return lambda x: bool(re.search(p,str(x)))

def only(patt,strs):
    _ = genPatt(patt)
    _ = filter(_, strs)
    return list(_)
def TableForm(lst):
    print(*lst, sep='\n')
    
    
    
    
class Slash2:
    def __init__(self, fn):
        self.fn = fn

    def __rfloordiv__(self, other):
        return self.fn(other)    
    
    
    
# Print = Slash2(print)
# Sum = Slash2(sum)
# [1, 2, 3]//Sum//Print
# ["This is great", 0.002, 3000.0002,1.2333]//Slash2(tableform)
