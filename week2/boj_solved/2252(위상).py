import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

visited = []
stack = []
for i in range(1,len(indegree)):
    if indegree[i] == 0:
        stack.append(i)
while stack:
    tall = stack.pop()
    visited.append(tall)
    for j in graph[tall]:
        indegree[j] -= 1
        if indegree[j] == 0:
            stack.append(j)
print(*visited)