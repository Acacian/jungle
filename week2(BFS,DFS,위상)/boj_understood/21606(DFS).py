from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def DFS(v:int): # 깊이우선 탐색
    indoor = 0
    for i in net[v]:
        if A[i-1] == 0:
            if i not in visited:
                visited.add(i)
                indoor += DFS(i)
        else: indoor += 1

    return indoor

N = int(input())
A = list(map(int, list(input()))) # 장소 n에 대하여 A[n-1]이 1이면 실내, 0이면 실외.
net = defaultdict(list)
route_count = 0

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    net[u].append(v)
    net[v].append(u)
    if A[u-1] == 1 and A[v-1] == 1:
        route_count += 2 # 실내끼리 인접했을 경우 경로를 2개 더해준다.

visited = set()
for i in range(1, N+1):
    indoor = 0
    if A[i-1] == 0:
        if i not in visited:
            visited.add(i)
            indoor = DFS(i)

    route_count += indoor*(indoor-1)

print(route_count)

# import sys
# input = sys.stdin.readline

# N = int(input())
# A = list(str(input().rstrip()))

# graph = [[0] * (N+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     graph[i][0] = int(A[i-1])
#     graph[0][i] = int(A[i-1])

# for i in range(len(A)-1):
#     a,b = map(int,input().split())
#     graph[a][b] = graph[b][a] = 1

# visited = [0] * (N+1)

# def dfs(N):
#     count = 0
#     visited[N] = 1
#     for i in range(1, N+1):
#         if graph[N][i] == 1 and visited[i] == 0 and graph[i][0] == 1:
#             count += 1
#             dfs(i)

#     print(count, end=' ')

# for i in range(1, N+1):
#     if graph[i][0] == 1:
#         dfs(i)