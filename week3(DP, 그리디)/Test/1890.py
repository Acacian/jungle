import sys
input = sys.stdin.readline

N = int(input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

graph = [[0] * (N) for _ in range(N)]

for i in range(N):
    for j in range(N):
        graph[i][j] = graph

