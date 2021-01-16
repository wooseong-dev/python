class HashTable:
    
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
        
    def hash_function(self, key):
        return key % 8
    
    def print(self):
        print(self.hash_table)
        
    def insert(self, key, value):
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value
        
    def read(self, key):
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]
        
ht1=HashTable()
ht1.insert(1, 'a')
ht1.insert(2, 'b')
ht1.insert(3, 'c')
ht1.insert(4, 'd')
ht1.insert(5, 'e')
ht1.insert(6, 'f')
ht1.insert(7, 'g')
ht1.insert(8, 'h')

ht1.print()
