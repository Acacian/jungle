import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [1e9] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append((b , 1)) # 가중치 따로 있으면 그거 넣으면 됨

def djk(start):
    answer = []
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist : continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

    for j in range(1, N+1):
        if distance[j] == K : answer.append(j)
    if len(answer) == 0 : print(-1)
    else : 
        for k in answer : print(k, end='\n')
djk(X)

