import sys
import heapq 

input = sys.stdin.readline

R, S = map(int, (input().split()))
graph = [[0] * (R+1) for _ in range(S+1)]

for x in range(R):
    for y in range(S):
        if map[y][x] == '*':
            