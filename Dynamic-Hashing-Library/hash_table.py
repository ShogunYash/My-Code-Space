from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        self.params = params
        self.size = params[-1]
        self.table = ["<EMPTY>"] * self.size
        self.count = 0

    def hash_fxn(self, key, z, mod):
        fxn = 0
        for i in range(len(key) - 1, -1, -1):
            p = ord(key[i]) - (39 if key[i].isupper() else 97)
            fxn = (fxn * z + p) % mod
        return fxn

    def insert(self, x):
        if self.collision_type == "Chain":
            self.chain_insert(x)
        elif self.collision_type == "Linear":
            self.linear_insert(x)
        elif self.collision_type == "Double":
            self.double_insert(x)
        pass

    def chain_insert(self, x):
        z = self.params[0]
        index = self.hash_fxn(x, self.params[0], self.size)
        if self.table[index] == "<EMPTY>":
            self.table[index] = []
        if x not in self.table[index]: 
            self.table[index].append(x)
            self.count += 1 

    def linear_insert(self, x):
        if self.count == self.size:
            raise Exception("Table is full")
        index = self.hash_fxn(x, self.params[0], self.size)
        while self.table[index] != "<EMPTY>":
            if self.table[index] == x:
                return
            index = (index + 1) % self.size
        self.table[index] = x
        self.count += 1

    def double_insert(self, x):
        if self.count == self.size:
            raise Exception("Table is full")
        index1 = self.hash_fxn(x, self.params[0], self.size)
        index2 = self.params[2] - self.hash_fxn(x, self.params[1], self.params[2])
        index = index1
        while self.table[index] != "<EMPTY>":
            if self.table[index] == x:
                return
            index = (index + index2) % self.size
        self.table[index] = x
        self.count += 1

    def find(self, key):
        index = self.hash_fxn(key, self.params[0], self.size)
        if self.collision_type == "Chain": 
            if self.table[index] != "<EMPTY>":
                return key in self.table[index]
        elif self.collision_type == "Linear":
            start = index
            while self.table[index] != "<EMPTY>": 
                if self.table[index] == key:
                    return True
                index = (index + 1) % self.size
                if index == start:
                    break
            return False
        else:
            index2 = self.params[2] - self.hash_fxn(key, self.params[1], self.params[2])
            start = index
            while self.table[index] != "<EMPTY>":
                if self.table[index] == key:
                    return True
                index = (index + index2) % self.size
                if index == start:
                    break
            return False
    
    def get_slot(self, key):
        index = self.hash_fxn(key,self.params[0],self.size)
        return index
    
    def get_load(self):
        return self.count / self.size
    
    def __str__(self):
        if self.collision_type == "Chain":
            return " | ".join([" ; ".join(item) if item != "<EMPTY>" else "<EMPTY>" for item in self.table])
        else:
            return " | ".join((item) for item in self.table)
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, key):
        super().insert(key)
        pass
    
    def find(self, key):
        return super().find(key)
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return super().get_load()
    
    def __str__(self):
        return super().__str__()
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, x):
        # x = (key, value)
        if self.collision_type == "Chain":
            self.chain_insert(x)
        elif self.collision_type == "Double":
            self.double_insert(x)
        else:
            self.linear_insert(x)
        pass
    
    def chain_insert(self, x):
        key , value = x
        index = super().hash_fxn(key, self.params[0], self.size)
        if self.table[index] == "<EMPTY>":
            self.table[index] = []
        for k, v in self.table[index]:
            if k == key:
                return
        self.table[index].append(x)
        self.count += 1
        pass

    def linear_insert(self, x):
        if self.size == self.count:
            raise Exception ("Table is full")
        index = super().hash_fxn(x, self.params[0], self.size)
        key, value = x
        while self.table[index] != "<EMPTY>":
            if self.table[index][0] == key :
                return
            index = (index + 1) % self.size
        self.table[index] = x
        self.count += 1

    def double_insert(self, x):
        if self.size == self.count:
            raise Exception("Table is full")
        key , value = x
        index = super().hash_fxn(x, self.params[0], self.size)
        index2 = super().params[2] - self.hash_fxn(x, self.params[1], self.params[2])
        while self.table[index] != "<EMPTY>":
            if self.table[index][0] == key:
                return
            index = (index + index2) % self.size
        self.table[index] = x
        self.count += 1
        pass

    def find(self, key):
        index = super().hash_fxn(key, self.params[0], self.size)
        if self.collision_type == "Chain":
            if self.table[index] != "<EMPTY>":
                for k, v in self.table[index]:
                    if k == key:
                        return v
            return None
        elif self.collision_type == "Linear":
            start = index
            while self.table[index] != "<EMPTY>":
                if self.table[index][0] == key:
                    return self.table[index][1]
                index = (index + 1) % self.size
                if index == start:
                    break
            return None
        else:
            index2 = self.params[2] - self.hash_fxn(key, self.params[1], self.params[2])
            start = index
            while self.table[index] != "<EMPTY>":
                if self.table[index][0] == key:
                    return self.table[index][1]
                index = (index + index2) % self.size
                if index == start:
                    break
            return None
    
    def get_slot(self, key):
        return super().get_slot(key)
    
    def get_load(self):
        return self.count / self.size
    
    def __str__(self):
        if self.collision_type == "Chain":
            for item in self.table:
                if item == "<EMPTY>":
                    continue
                for entry in item:
                    print(entry[0] + ": " + entry[1].__str__())
        else:
            for item in self.table:
                if item == "<EMPTY>":
                    continue
                print(item[0] + ": " +item[1].__str__())

    def rehash(self):
        pass

