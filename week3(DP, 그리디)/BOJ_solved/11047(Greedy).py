import sys
input = sys.stdin.readline

N,K = map(int, input().split())

C = [[0] * N for _ in range(N)]
count = 0
for j in range(N):
    C[j] = int(input())

for i in range(N-1,-1, -1):
    count += K // C[i]
    K = K % C[i]

print(count)