class A:                              # inheritance grandparent
    def f1(self):
        print("F1 working")


class B(A):                           #inheritance child/parent class
    def f2(self):
        print("F2 working")

class C(B):                           #inheritance grandchild
    def f3(self):
        print("F3 working")

c1=C()
print(c1.f1())