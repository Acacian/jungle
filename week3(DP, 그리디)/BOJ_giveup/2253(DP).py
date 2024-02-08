from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)

#https://velog.io/@grace0st/%EC%A0%90%ED%94%84-%EB%B0%B1%EC%A4%80-2253%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC



# import sys
# N, M = map(int, sys.stdin.readline().split())
# dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
# dp[1][0] = 0

# stone_set = set()
# for _ in range(M):
#     stone_set.add(int(sys.stdin.readline()))
# for i in range(2, N + 1):
#     if i in stone_set:
#         continue
#     for j in range(1, int((2 * i) ** 0.5) + 1):
#         dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

# if min(dp[N]) == float('inf'):
#     print(-1)
# else:
#     print(min(dp[N]))