import dummy

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


class X:
    a = 0.0
    b = 0.0
    c = 0.0

    def __init__(self, ain, bin, cin):
        self.a = ain
        self.b = bin
        self.c = cin

    def print(self):
        print("(", self.a, r"\frac{x}{y}", self.b, ",", self.c, ",", ")")
