n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int,input().split()))

# graph = [0] * N
# for i in range(N):
#     this = arr[i] * (N // (i+1))
#     if N % (i+1) > 0:
#         tray = arr[((N % (i+1))-1)]
#         this += max(tray , ((N % (i+1))-1) // 2
#     graph[i] = max(this, graph[i-1])

# print(max(graph))

# # + arr[(10 % (i+1))]