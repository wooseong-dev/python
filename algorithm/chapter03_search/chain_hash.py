class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])
    def hash_function(self, key):
        return key%8
    
    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)
        
        if self.hash_table[hash_value]!=0:
            #해당 hash_value를 이미 사용하고 있는 경우(충돌할 경우)
            for i in range(len(self.hash_table[hash_value])):
                #이미 같은 키 값이 존재할 경우 -> value 교체
                #이때 0은 key, 1은 value 값이 존재하는 인덱스
                if self.hash_table[hash_value][i][0] == gen_key:
                    self.hash_table[hash_value][i][1] = value
                    return
            #같은 키 값이 존재하지 않을 경우 [key, value] 를 해당 인덱스에 삽입
            self.hash_table[hash_value].append([gen_key, value])
        else:
            #해당 hash_value를 사용하고 있지 않는 경우
            self.hash_table[hash_value] = [[gen_key, value]]
            
            
    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)
        
        if self.hash_table[hash_value] != 0:
            #해당 해쉬값 index 에 데이터가 존재할때
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    #키와 동일할 경우 -> 해당 value return
                    return self.hash_table[hash_value][i][1]
                #동일한 키가 존재하지 않으면 None return
                return None
            else:
                #해당 해쉬 값 index 에 데이터가 없을 때
                return None
    def print(self):
        print(self.hash_table)
                
                
ht = HashTable()
ht.insert(1, 'a')
ht.print() 
ht.insert('name', 'kang')
ht.print() 
ht.insert(2, 'b')
ht.print()
ht.insert(3, 'c')
ht.print()
print(ht.read(2))
ht.insert(4, 'd')
ht.print()
                
                
                
                
                