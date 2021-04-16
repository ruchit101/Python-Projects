# def fun(n):
#     for i in range(n):  # It will produce the iterations whenever required
#         yield i                    # It will not create iterations and store in memory
#                             # #its just generates it when .__next__() is used.
#
# f=fun(5)
# print(f.__next__())
# print(f.__next__())
# print("Ruchit Bagaade ")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
no_of_list = int(input("How many items add in a list: "))
input_string = input("Enter a list element separated by space ")
list = input_string.split()
t = int(input("Which type of comprehension you use 1. List Comprehension 2.Dictionary Comprehension 3. Set Comprehension "))
if t==1:
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t==2:
    dict1 = {f'item{i}': i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s ={i for i in list}
    print(s)
    print(type(s))