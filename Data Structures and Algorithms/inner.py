class Student:

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.sub = self.Subject()

    def show(self):
        print(self.m1, self.m2, self.m3)
        self.sub.show()

    class Subject:
        def __init__(self):
            self.sub1 = "English"
            self.sub2 = "hindi"
            self.sub3 = "Marathi"

        def show(self):
            print(self.sub1, self.sub2, self.sub3)


s1 = Student(74, 87, 95)
# we can also create object of the inner class outside
# like lap1=student.Laptop()
s1.show()
