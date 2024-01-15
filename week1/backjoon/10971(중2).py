import sys

# 시작도시, 현재도시, 비용, 방문 도시 수
def dfs(start, now, value, cnt):
    global ans
    # 현재까지 이동 비용이 이미 알려진 최소비용보다 크다면 종료
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N

# 깊이 우선 탐색 함수 호출
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)