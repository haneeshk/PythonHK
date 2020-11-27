from IPython.display import display, Math
class X:
    __data = []

    def __init__(self, ain, bin, cin):
        self.__data = [ain,bin,cin]
    def __getitem__(self,i: int) -> float:
        if i<1 or i>3:
            raise IndexError("Index out of bounds")
        return self.__data[i-1]

    def print(self):
        d="\\left(\\begin{align}"+str(self.__data[0])+"\\\\"+str(self.__data[1])+"\\\\"+str(self.__data[2])+"\\end{align}\\right)"
        display(Math(d))
