from __future__ import annotations
import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key):
        if isinstance(key,int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None
    
    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False
    
    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            print(i,end='')
            while p is not None:
                print(p.key , p.value)
                p = p.next
            print()

if __name__ == "__main__":
    # ChainedHash 객체 생성 (예: capacity = 10)
    hash_table = ChainedHash(10)

    # 데이터 추가
    hash_table.add("apple", 1)
    hash_table.add("banana", 2)
    hash_table.add("cherry", 3)

    # 데이터 검색
    result = hash_table.search("banana")
    print("Search Result for 'banana':", result)

    # 데이터 제거
    removed = hash_table.remove("banana")
    print("Remove Result for 'banana':", removed)

    # 해시 테이블 출력
    print("Hash Table Dump:")
    hash_table.dump()

## 답 
# from __future__ import annotations
# from typing import Any, Type
# import hashlib

# class Node:
#     def __init__(self, key : Any, value : Any , next : Node) -> None:
#         self.key = key
#         self.value = value
#         self.next = next

# class ChainedHash:
#     def __init__(self, capacity: int) -> None :
#         self.capacity = capacity
#         self.table = [None] * self.capacity

#     def hash_value(self, key : Any) -> int:
#         if isinstance(key,int):
#             return key % self.capacity
#         return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
#     def search(self, key : Any) -> Any:
#         hash = self.hash_value(key)
#         p = self.table[hash]
#         while p is not None:
#             if p.key == key:
#                 return p.value
#             p = p.next

#         return None
    
#     def add(self, key : Any, value : Any) -> bool:
#         hash = self.hash_value(key)
#         p = self.table[hash]
#         while p is not None:
#             if p.key == key:
#                 return False
#             p = p.next

#         temp = Node(key, value, self.table[hash])
#         self.table[hash] = temp
#         return True
    
#     def remove(self, key : Any) -> bool:
#         hash = self.hash_value(key)
#         p = self.table[hash]
#         pp = None

#         while p is not None:
#             if p.key == key:
#                 if pp is None:
#                     self.table[hash] = p.next
#                 else:
#                     pp.next = p.next
#                 return True
#             pp = p
#             p = p.next
#         return False
    
#     def dump(self) -> None:
#         for i in range(self.capacity):
#             p = self.table[i]
#             print(i,end='')
#             while p is not None:
#                 print(p.key , p.value)
#                 p = p.next
#             print()