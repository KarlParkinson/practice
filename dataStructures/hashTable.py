class HashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None]*size
        self.data = [None]*size

    def put(self, key, data):
        hashValue = self._hash(key)
        if (self.keys[hashValue] == None):
            # no collision, found empty slot, so insert
            self.keys[hashValue] = key
            self.data[hashValue] = data
        elif (self.keys[hashValue] == key):
            # no collision, found spot, replace old data
            self.data[hashValue] = data
        else:
            hashValue = self._rehash(hashValue)
            while (self.keys[hashValue] != None and self.keys[hashValue] != key and self.keys[hashValue] != 'deleted'):
                hashValue = self._rehash(hashValue)
            if (self.keys[hashValue] == None or self.keys[hashValue] == 'deleted'):
                # found empty slot, insert data
                self.keys[hashValue] = key
                self.data[hashValue] = data
            else:
                # found slot, replace data
                self.data[hashValue] = data


    def get(self, key):
        hashValue = self._hash(key)
        found = False
        stop = False
        startPos = hashValue
        while (self.keys[hashValue] != None and not found and not stop):
            if (self.keys[hashValue] == key):
                found = True
            else:
                hashValue = self._rehash(hashValue)
                if (hashValue == startPos):
                    stop = True
        if (found):
            return self.data[hashValue]
        else:
            return None

    def delete(self, key):
        hashValue = self._hash(key)
        found = False
        stop = False
        startPos = hashValue
        while (self.keys[hashValue] != None and not found and not stop):
            if (self.keys[hashValue] == key):
                found = True
            else:
                hashValue = self._rehash(hashValue)
                if (hashValue == startPos):
                    stop = True
        if (found):
            self.keys[hashValue] = 'deleted'
            self.data[hashValue] = None
        else:
            return False

    def _hash(self, key):
        return key % self.size

    def _rehash(self, hashValue):
        return (hashValue+1) % self.size
            


h = HashTable(11)
h.put(1,3)
h.put(12,5)
h.put(23, 78)
print h.keys
h.delete(12)
print h.get(1)
print h.get(23)
print h.keys
h.put(34, 35)
print h.keys
print h.data
#h.put(5,6)
#h.put(7,9)

