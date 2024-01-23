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
    visited2[V] = 1 # 간 곳 체크(기본적으로 1에서 시작하므로 1로 설정)
    while queue:
        V = queue.pop(0) # 큐에 넣은 노드를 없애면서 차례대로 돔.
        print(V, end = '')
        for i in range(1, N + 1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)  # 인접한 모든 노드를 큐에 추가함. 만약 이동한 경우,(예를 들어 1>2) 이미 2가 queue에 있기 때문에 2를 또 queue에 추가하지 않음.
                # 일단 시작 노드인 1이 queue에 추가. 이후 queue에서 1을 빼면서 1을 출력 > 1과 인접한 노드인 2,3,4가 queue에 추가됨. 그럼 큐에는 2,3,4가 있고 이 중에서 처음으로 2가 빠짐.
                # 즉, 경로 상 1이 있는 곳은 값이 낮은 순서대로 전부 추가한다고 보면 됨.
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