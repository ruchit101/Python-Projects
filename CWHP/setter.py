# class B:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#         self.email=l+b
#         # self.email = self.l + self.b     # Not possible. Need to use the Setter (Kageyama)
#     @property
#     def printemail(self):
#         self.email = self.l + self.b
#         return self.email
# bob=B(5,10)
# print(bob.email)
# bob.l=20
# print(bob.l)
# print(bob.email) # function bane attribute
# print(bob.printemail) # use it as a attribute
#


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email) # we are accessing the "email" @property method
hindustani_supporter.email = "this.that@codewithharry.com" # we are accessing the "email" @email.setter method
print(hindustani_supporter.fname)

del hindustani_supporter.email # we are accessing the "email" @email.deleter method
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)
