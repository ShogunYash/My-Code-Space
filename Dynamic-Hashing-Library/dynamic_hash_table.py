from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        self.size = get_next_size()
        self.table = ["<EMPTY>"] * self.size
        self.count = 0
        if self.collision_type == "Chain":
            for item in old_table:
                if item == "<EMPTY>":
                    continue
                for x in item:
                    self.insert(x)
        else:
            for item in old_table:
                if item == "<EMPTY>":
                    continue
                self.insert(item)
        pass

    def insert(self, x):
        super().insert(x)
        
        # Rehash if load factor exceeds threshold
        if self.get_load() >= 0.5:
            self.rehash()
                     
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        self.size = get_next_size()
        self.table = ["<EMPTY>"] * self.size
        self.count = 0
        if self.collision_type == "Chain":
            for item in old_table:
                if item == "<EMPTY>":
                    continue
                for x in item:
                    self.insert(x)
        else:
            for item in old_table:
                if item == "<EMPTY>":
                    continue
                self.insert(item)
        pass

    def insert(self, key):
        super().insert(key)
        
        # Rehash if load factor exceeds threshold
        if self.get_load() >= 0.5:
            self.rehash()
