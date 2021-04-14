# Polymorphism
class student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a + b + c
            return s
        elif a != None and b != None:
            s = a + b
            return s
        else:
            return a


a1 = student(54, 78)

print(a1.sum(4))
print(a1.sum(4,9))
print(a1.sum(4,7,5))


#Oveerriding

class A:
    def show(self):
        print('In A')

class B(A):
    pass

    #def show(self):
     #   print('In B ab A ki jarurat nahi')


a1=B()
a1.show()