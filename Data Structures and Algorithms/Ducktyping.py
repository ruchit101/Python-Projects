# duck typing
class Pycharm:

    def execute(self):
        print("Pycharm it is! ")


class Neweditor:

    def execute(self):
        print("New one it is!")


class Laptop:
    def code(self, ide):
        ide.execute()


ide2 = Neweditor()
ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)
#print(Laptop.code(lap1,ide))
