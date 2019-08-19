class HashTable:
    def __init__(self):
        self.size = 3
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def get_hash(self, key):
        if type(key) == int or type(key) == float:
            return key % self.size
        elif type(key) == str:
            sum_asci = 0
            for i in key:
                sum_asci = sum_asci + ord(i)
            return  sum_asci % self.size

    def rehash(self, oldhash):
        next_hash = (oldhash + 1) % self.size
        return next_hash

    def put(self, key, data):
        index = self.get_hash(key)

        if self.keys[index] == None:
            self.keys[index] = key
            self.values[index] = data
        else:
            if self.keys[index] == key:
                self.values[index] = data
            else:
                next_index = self.rehash(index)

                while self.keys[next_index] != None and self.keys[next_index] != key:
                    if index == next_index:
                        self.size +=1
                        self.keys.append(None)
                        self.values.append(None)

                    next_index = self.rehash(next_index)

            if self.keys[next_index] == None:
                self.keys[next_index] = key
                self.values[next_index] = data
            else:
                self.values[next_index] = data


    def get(self, key):
        start_index = self.get_hash(key)
        position = start_index
        data = None
        search = True

        while self.keys[position] != None and search:
            if self.keys[position] == key:
                search = False
                data = self.values[position]
            else:
                position = self.rehash(position)
                if position == start_index:
                    search = False
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        index = self.get_hash(key)
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
        else:
            next_index  = self.rehash(index)
            while self.keys[next_index] != None and self.keys[next_index] != key:
                next_index = self.rehash(next_index)

            self.keys[next_index] = None
            self.values[next_index] = None

    def print_hashtable(self):
        print(dict(zip(self.keys, self.values)))
