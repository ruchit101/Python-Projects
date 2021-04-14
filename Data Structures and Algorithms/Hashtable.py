#O(1) is the order of Dictionary here what we do we have key and we use the hash function to get the
#adresss for the value to be stored.
#
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None



t = HashTable()
t['March 6']=12
t['March 17']=1457
print(t['March 6']) # this overwrite happened this is called as Collision
#To handle collisions we have diferenct techniquies
# Separate Chaining
# Linear Probing

