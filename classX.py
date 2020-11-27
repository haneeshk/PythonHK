from IPython.display import display, Math
class X:
    a = 0.0
    b = 0.0
    c = 0.0

    def __init__(self, ain, bin, cin):
        self.a = ain
        self.b = bin
        self.c = cin

    def print(self):
        d="\\left(\\begin{align}"+str(self.a)+"\\\\"+str(self.b)+"\\\\"+str(self.c)+"\\end{align}\\right)"
        display(Math(d))
