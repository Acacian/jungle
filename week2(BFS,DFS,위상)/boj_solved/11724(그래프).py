import sys
input = sys.stdin.readline
from collections import deque

N , M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (N+1)

count = [0]
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        start = queue.popleft()
        for i in range(1, N+1):
            if (graph[start][i] == 1 and visited[i] == 0):
                visited[i] = 1
                queue.append(i)
    if not queue:
        count[0] += 1
        for i in range(1, N+1):
            if visited[i] == 0:
                bfs(i)
    if visited.count(0) == 1:
        return count[0]

bfs(1)
print(count[0])