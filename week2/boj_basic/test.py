N,M,V = map(int,input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (N+1)
visited2 = visited1.copy() # BFS용

def dfs(V):
    visited1[V] = 1 #간 곳 체크하는거
    print(V, end = '')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1 # 간 곳 체크
    while queue:
        V = queue.pop(0) # 간 노드 제거
        print(V, end = '')
        for i in range(1, N + 1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1


dfs(V)
print()
bfs(V)







# def dfs(graph , v, visited):
#     visited[v] = True
#     print(v,end = '')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i , visited)

# graph = ...

# visited = [False] * 9
# dfs(graph,1,visited)

##############////

# def bfs(graph , v, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = ...

# visited = [False] * 9
# bfs(graph,1,visited)