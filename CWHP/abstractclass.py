from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta): # hence the class is known as Abstract class

    @abstractmethod         # Makes mandatory to create this abstract method in each and every child class
    def printarea(self):    # Basically a dad(Parent Class) is teaching his child(Child Class)
        return None         # to follow some rituals forcefully.



class B(A):
    def __init__(self):
        self.l = 10
        self.b = 5

    def printarea(self):
        return self.l * self.b


b = B()
print(b.printarea())
