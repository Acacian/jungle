import sys
input = sys.stdin.readline

N = int(input())
arr = [0]

for _ in range(N):
    arr.append(int(input()))

arr.append(0)
arr.append(0)
graph = [0] * (N+1)

for i in range(3,N+1):
    if N > 1:
        graph[1] = arr[1]
    if N > 2:
        graph[2] = arr[2] + arr[1]

    if arr[i+1] < arr[i+2]:
        arr[i+1] = 0

    graph[i] = graph[i-2] + max(arr[i-2] + arr[i] , arr[i-1] + arr[i])

print(graph[N])
