class Student:
    school="Timshenko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_school(cls):
        return print(cls.school)

s1=Student(47,84,45)
s2=Student(90,74,54)
print(s1.m1)
print(s1.avg())
print(s2.avg())
print(s1.get_school())