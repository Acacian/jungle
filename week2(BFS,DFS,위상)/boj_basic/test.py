import sys
input = sys.stdin.readline
import heapq

N , M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a,b = (map(int, input().split()))
    graph[a].append(b)
    indegree[b] += 1

heap = []
answer = []
for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    a = heapq.heappop(heap)
    answer.append(a)
    for i in graph[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)
if len(answer) == N:
    print(*answer)