import dummy
import mypy
! pip install mypy
x = dummy.func1(22.0)
x


x = func1(22)
print(x)

X1 = X(0.2, 0.2, 0.3)
X1.a = 0.2
X1.b = 0.3
X1.c = 0.5
X1.print()
X1.a
txte = r"The \emph{characteristic polynomial} $\chi(\lambda)$ of the $3 \times 3$~matrix \\ $\left( \begin{array}{ccc} a & b & c \\ d & e & f \\g & h & i \end{array} \right) $ \\is given by the formula\\ $ \chi(\lambda) = \left| \begin{array}{ccc} \lambda - a & -b & -c \\ -d & \lambda - e & -f \\ -g & -h & \lambda - i \end{array} \right|. $"
print(txte)
from IPython.display import display, Math
display(Math(r'$x^2$'))
display(Math(r'$$\mathcal{x}$$'))
class X:
    a = 0.0
    b = 0.0
    c = 0.0

    def __init__(self, ain, bin, cin):
        self.a = ain
        self.b = bin
        self.c = cin

    def print(self):
        display(Math("(", self.a, r"\frac{x}{y}", self.b, ",", self.c, ",", ")"))



funTensor(a:X)->double:
    return   a.a