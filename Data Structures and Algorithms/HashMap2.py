# O(1) is the order of Dictionary here what we do we have key and we use the hash function to get the
# adresss for the value to be stored.
#
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # self.arr[h] = value  Stop overwriting and do 'CHAINING'
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)  # only value is we are trying to change
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for e in self.arr[h]:
            if e[0] == key:
                return e[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx , element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]


t = HashTable()
t['March 6'] = 120
t['March 17'] = 1457
print(t.arr)  # this overwrite happened this is called as Collision
# To handle collisions we have different  techniques
# Separate Chaining
# Linear Probing
print(t['March 6'])
del t['March 6']
print(t.arr)

