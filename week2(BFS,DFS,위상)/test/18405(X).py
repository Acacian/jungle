import sys
input = sys.stdin.readline
import heapq

N,M = map(int,(input().split()))
graph = [[] for _ in range(N+1)]
arr = []
q = ()
q.append(())

for _ in range(N):
    arr.append(list(map(list, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(arr)