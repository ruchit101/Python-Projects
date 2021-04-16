class A:
    def __init__(self, sal):
        self.salary = sal
        # methods having two underscores @ prefix and suffix are dunder methods

    def __add__(self, other):
        return self.salary / other.salary

    def __truediv__(self, other):
        return self.salary + other.salary

    def __mul__(self, other):
        return self.salary - other.salary

    def __sub__(self, other):
        return self.salary + other.salary


a = A(500)
b = A(600)

print(a + b)
print(a / b)
print(a * b)
print(a - b)
