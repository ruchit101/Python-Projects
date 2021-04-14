class car:
    wheels = 4
    def __init__(self):
        self.mil="10"
        self.com='BMW'

c1=car()
c2=car()

c1.com=1000

car.wheels= 2
print(c1.com , car.wheels)
print(c2.mil)