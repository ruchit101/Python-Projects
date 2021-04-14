import random
charac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
length = int(input("ENTER THE LENGTH OF THE PASSWORD: "))
password=""
for i in range(1,length+1):
    password+= random.choice(charac)
print(password)
