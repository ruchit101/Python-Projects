# Doesnt support directly
# hence to make a class abstract import ABC
# abstract methd is the method with declaration but with no defination
# class with abstract method is called abstract class

from abc import ABC, abstractmethod


class C(ABC):
    @abstractmethod
    def a(self):
        pass


# com=C()
# com.a()
# a is the abstract method
# You cant create the object of the abstract class

class Laptop(C):
    def a(self):
        print('Its Running')

class White:
    def b(self):
        print('Its writing')

class Prog:
    def c(self,com):
        print(" Solov")
        com.a()
cc=Laptop()
w=White()
p=Prog()
p.c(w)