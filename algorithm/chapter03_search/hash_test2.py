class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)]) #0으로만 이루어진 8자리의 리스트
         
    def hash_function(self, key):
        return key % 8 # 해쉬테이블에 8자리의 공간
    
    def insert(self, key, value): # key와 value를 넣을 수 있다.
        hash_value = self.hash_function(hash(key))
        self.hash_table[hash_value] = value
        
    def read(self,key): # key값을 이용하여 value값을 얻을 수 있다.
        hash_value = self.hash_function(hash(key))
        return self.hash_table[hash_value]
    
    def print(self):
        print(self.hash_table)
        
        #hash함수는 랜덤연산작용으로 실행시마다 값이 달라짐
        
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
# 충돌이 발생해서 ('name','kang') 쌍이 삭제를 안함에도 불구하고
# (2, 'b') 쌍이 들어가자 없어졌다 이는 hash의 계산 값이 겸침으로 인한 충돌이 발생했다
#https://davinci-ai.tistory.com/19

