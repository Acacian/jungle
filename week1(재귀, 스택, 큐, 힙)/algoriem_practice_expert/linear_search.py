from typing import Any, Sequence

def seq_search(a : Sequence, key : Any) -> int:
    i = 0
    while True:
        #다 끝났는데 안 나오면 종료
        if i == len(a):
            return -1
        #검색값 찾으면 종료
        if a[i] == key:
            return i
        i += 1

num = int(input())
x = [None] * num
for i in range(num):
    x[i] = int(input())

ky = int(input())

idx = seq_search(x,ky)

if idx != -1:
    print(idx)
