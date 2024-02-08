import sys
input = sys.stdin.readline
import heapq

V , E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,value = map(int, input().split())
    graph[a].append([value,b])
    graph[b].append([value,a])

heap = [[0,1]]
visit = [0] * (V+1)


answer = 0
while heap:
    val, now = heapq.heappop(heap)
    if not visit[now]:
        visit[now] = 1
        answer += val
        for i in graph[now]:
            heapq.heappush(heap,i)
print(answer)

            

# import sys
# input = sys.stdin.readline

# V , E = map(int, input().split())
# graph = [[] for _ in range(V+1)]
# for i in range(E):
#     a,b,value = map(int, input().split())
#     graph[a].append((b,value))

# stack = []
# visited = [1e9] * (V+1)

# def spn(n):
    
#     stack.append((0,n))
#     while stack:
#         val, now = stack.pop()
#         if visited[now] > val:
#             visited[now] = val

#             for i in graph[now]:
#                 cost = val + i[1]
#                 if cost < visited[i[0]]:
#                     visited[i[0]] = cost
#                     stack.append((cost, i[0]))
#     print(cost)
#     exit
            

# spn(1)
