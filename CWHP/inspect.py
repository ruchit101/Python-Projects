class raj:
    def __init__(self,Name,Roll):
        self.Name = Name
        self.Roll = Roll

    def maine(self):
        return  f"My Name is {self.Name} And My Roll is {self.Roll}"


ra = raj("Raj",15)
print(type(ra))
print(id(ra))

a = "I am a good boy"
print(id(a))

print(dir(raj))

import inspect

print(inspect.getmembers(ra))