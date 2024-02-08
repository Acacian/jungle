graph = {}
visited = []
def dfs(v):
    visited.append(v)
    for _ in graph[v]:
        if v not in visited:
            dfs(v)

dfs('A')