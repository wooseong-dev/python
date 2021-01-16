from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    #해시 구성 노드
    def __init__(self, key:Any, value: Any, next : Node)->None:
        #초기화
        self.key = key
        self.value = value
        self.next = next
        
class ChainedHash:
    # 체인법 해시
    def __init__(self, capacity: int)-> None:
        self.capacity = capacity
        self.table = [None] * self.capacity #해시 테이블 크기의 리스트 생성
    
    def hash_value(self, key: Any) ->int:
        # 해시를 구함
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode().hexdigest(), 16)%self.capacity)
    def search(self, key:ANy)->Any:
        #키가 key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key) #검색하는 키의 해시값
        p = self.table[hash]        #노드를 주목
        
        while p is not None:
            if p.key == key:
                return p.value # 검색 성공시
            p = p.next # 뒤쪽 노드로 주목
                
        return None # 검색 실패
                
        
    def add(self, key:Any, value: Any)->bool:
                #키가 key이고 value인 원소를 추가
        hash = self.hash_value(key) # 추가할 key 의 해시값
        p = self.table[hash]  # 노드를 주목
        
        while p is not None:
                if p.key == key:
                    return false # 추가 실패
                p = p.next # 뒤쪽 노드로
                
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp # 노드를 추가
        return True             # 추가 성공
    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key):
        p = self.table[hash]
        pp=None
        
        while p is not None:
                if p.key == key:
                    if pp is None:
                        self.table[hash] = p.next
                    else:
                        pp.next = p.next
        
                
        
        