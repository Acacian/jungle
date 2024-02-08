import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int,(input().split()))
graph = [[0] * (N+1) for _ in range(N+1)]
arr = []

q = deque()
number = []

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] != 0:
            graph[i+1][j+1] = arr[i][j]
            q.append([i+1,j+1])
            number.append(arr[i][j])
# Sort기능추가        

S,X,Y = map(int,(input().split()))
number = sorted(number)
# 일단 첨에 들어갈 때는 sort한번 시켜줘야함

bx = [-1,1,0,0]
by = [0,0,-1,1]
counter = [0]

while q:
    x,y = q.popleft()
    num = number.pop(0)
    for i in range(4):
        a = x + bx[i]
        b = y + by[i]
        if 1 <= a <= N and 1 <= b <= N and graph[a][b] == 0:
            graph[a][b] = num
            q.append([a,b])
            number.append(graph[a][b])
    if num == 1 and num[-1] == K:
        counter[0] += 1
    if counter[0] == S:
        break
    
print(graph[X][Y])