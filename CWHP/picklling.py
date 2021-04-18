
import pickle
# packing th content in a file with different format 

# #Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)        # dump
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)        # load
print(mycar)
print(type(mycar))


# pickle.loads = ?




