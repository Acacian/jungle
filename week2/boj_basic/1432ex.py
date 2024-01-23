import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

N = int(input())
out_degree = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for i in range(1,N+1):
    temp = [0] + list(map(int,input().strip()))
    for j in range(1,N+1):
        if temp[j] == 1:
            out_degree[j].append(i)
            in_degree[i] += 1

answer = [0] * (N+1)

def sort():
    heaping = []
    for i in range(1,N+1):
        if in_degree[i] == 0:
            heapq.heappush(heaping,-i)

    NN = N
    while heaping:
        now = -heapq.heappop(heaping)
        answer[now] = NN
        for i in out_degree[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(heaping, -i)
        NN -= 1

sort()
if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])