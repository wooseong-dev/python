from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Statuc(Enum):
    OCCUPIED = 0 #데이터 저장
    EMPTY = 1 # 비어있음
    DELETED = 2 # 삭제 완료
    
class Bucket:
    def __init__(self, key: Any, value: Any=None,
                stat: Status = Status.Empty)->None:
        self.key = key
        self.value = value
        self.stat = stat
        
    def set(self, key:Any, value:Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat
    def set_status(self, stat: Status) -> None:
        self.stat = stat
        
class OpenHash:
    
    def __init__(self, capacity: int) ->None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity
    
    def hash_value(self, key:Any)->int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
               %self.capacity)
    def rehash_value(self, key:Any)->int:
        return(self.hash_value(key)+1)%self.capacity
    def search_node(self, key:Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
        
        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key