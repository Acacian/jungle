#from __future__ import annotations
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
            return key % self.capacity #정수일 경우 나머지 반환
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) #정수가 아닐 경우 SHA256해시 함수 사용해
        # 해싱 후 마찬가지로 capacity의 나머지를 반환
    
    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                #일치 시 반환
                return p.value
            # 아니면 이동
            p = p.next

        return None
    
    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            #지금 노트 키가 이미 존재하는가?
            if p.key == key:
                return False
            # 없다면 다음, 있다면 추가하지 않고 false반환
            p = p.next

        #새로운 노드를 생성하고, 해당 해시값에 있는 버킷의 맨 앞에 삽입
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                # 이전 노드가 없는 경우 현재 노드 p를 삭제하고, 테이블의 맨 앞을 업데이트
                if pp is None:
                    self.table[hash] = p.next
                else:
                # 만약 이전 노드가 있다면 현재 노드를 삭제하고 이전 노드의 next를 업데이트
                    pp.next = p.next
                #삭제가 성공적으로 이루어졌음을 나타내기 위해 true를 반환
                return True
            #일치하지 않을 시 이전 노드와 현재 노드를 업데이트
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