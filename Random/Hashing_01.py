def get_hash(key):
    h=0
    for char in key:
        h += ord(key)
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)
        return h %self.MAX