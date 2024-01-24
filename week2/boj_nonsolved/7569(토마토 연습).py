import sys
input = sys.stdin.readline
from collections import deque

X,Y,Z = map(int, input().split())
graph = []
queue = deque([])

for i in range(Z):
    time = []
    for j in range(Y):
        time.append(list(map(int, input().split())))
        for k in range(X):
            if time[j][k] == 1:
                queue.append([i,j,k]) # popleft라서 이 순서가 맞음
    graph.append(time)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while queue:
    x,y,z = queue.popleft()
    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]
        if 0 <= a < Z and 0 <= b < Y and 0 <= c < X and graph[a][b][c] == 0: #popleft라서 이렇게 저장함
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z] + 1

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)
