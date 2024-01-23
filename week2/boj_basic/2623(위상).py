import sys
input = sys.stdin.readline

N , M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    singer = list(map(int, input().split()))
    for s in range(1, singer[0]):
        graph[singer[s]].append(singer[s+1])
        indegree[singer[s+1]] += 1

visited = []
stack = []
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        stack.append(i)
while stack:
    fst = stack.pop()
    visited.append(fst)
    for j in graph[fst]:
        indegree[j] -= 1
        if indegree[j] == 0:
            stack.append(j)

if len(stack) == 0 and indegree[j] != 0:
    print(0)
else:
    print(*visited)