print("Just for Practice!!!!!")


class Player:
    def __init__(self, name, game, college):
        self.name = name
        self.game = game
        self.college = college


class Student(Player):
    def __init__(self, std):
        self.std = std
        super().__init__("Rahul","Cricket","IIT")


rahul = Student("4th")
print(rahul.name)
print(rahul.game)
print(rahul.college)
print(rahul.std)
