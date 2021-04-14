print('After a long time working ion python pycharm')
nums = [4,7,8,5,4,7,89,6,4,7,8,4]
evens = list(filter(lambda x: x%2==0,nums))
mapping=list(map(lambda x: x*2,evens))
print(evens)
print(mapping)
reduceing= reduce(lambda x,y: x+y,mapping)
print(reduceing)