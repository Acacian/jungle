import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,(input().split()))
graph = [[0] * (M) for _ in range(N)]
arr = []

for i in range(N):
    arr.append(list(map(list, input().rstrip())))
    for j in range(M):
        if arr[i][j] == ['-'] :
            graph[i][j] = 1
        else :
            graph[i][j] = 0

q = deque()
for j in range(N):
    q.append(graph[j])

count = [0]
visited = [0] * (M)

while q:
    rm = q.popleft()
    for i in range(len(rm)):
        if rm[i] == 1:
            count[0] += 1
            if rm[i-1] == 1 and i != 0:
                count[0] -= 1
            if rm[i] == 1 and visited[i] > 0:
                visited[i] = 0
        if rm[i] == 0:
            count[0] += 1
            visited[i] += 1
            if rm[i] == 0 and visited[i] > 1:
                count[0] -= 1

print(count[0])