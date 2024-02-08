import sys
from collections import deque
input = sys.stdin.readline

graph = []

Y, X = map(int, input().split())
for _ in range(Y):
    graph.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < X and 0 <= ny < Y and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[X-1][Y-1]

print(bfs(0,0))