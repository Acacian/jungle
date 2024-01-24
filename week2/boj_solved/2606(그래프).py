import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
visited[1] = 1
app = []

count = 0
def bfs(start):
    global count
    global app
    q = deque([start])
    while q:
        ql = q.popleft()
        for i in graph[ql]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                app.append(i)
                count += 1
    print(count)
    exit

bfs(1)