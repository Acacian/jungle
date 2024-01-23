import sys
input = sys.stdin.readline
from collections import deque

N , M , K , X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
distance = [0] * (N+1)
visited = [False] * (N+1)
for _ in range(M):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)

# print(graph)
def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i] :
                visited[i] = True
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end = '\n')

bfs(X)