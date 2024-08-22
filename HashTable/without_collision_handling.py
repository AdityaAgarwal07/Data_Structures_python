class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.Max

    def __setitem__(self, key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        print(self.arr[h])

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["dec 30"] = 88
t["march 7"]
t["march 6"]
print(t.arr)
del t["march 6"]
t["march 6"]
print(t.arr)