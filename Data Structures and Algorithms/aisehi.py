class computer:
    def __init__(self,cpu,hard):
        self.cpu=cpu
        self.hard=hard

    def config(self):
        print("Configuration is :",self.cpu,self.hard)

com1=computer("AMD",'1 TB')
com2=computer("Intel",'2 TB')

com1.config()
com2.config()