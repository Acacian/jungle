## 방법은 맞는데 이진탐색으로 풀어야함

n, m = map(int, input().split())
tree = list(map(int, input().split()))

# 이진 탐색을 위한 시작점, 끝점
start = 0
end = max(tree)

result = 0 # 최종 절단기 높이
while(start <= end):
    total = 0 # 가져갈 나무의 길이
    mid = (start + end) // 2 # 절단기 높이
    for i in tree:
        if i > mid: # 절단기보다 주어진 나무가 길면 자른 나머지를 total에 추가
            total += i - mid
            
    # 이진 탐색        
    if total < m: # 가져가야 하는 길이 m보다 작은 길이이면
        end = mid - 1 # mid 기준 왼쪽 부분 탐색
    else: # 가져가야 하는 길이 m보다 크거나 같으면
        result = mid # 절단기 높이를 mid로 설정
        start = mid + 1 # mid 기준 오른쪽 부분 탐색

print(result)


# NM = list(map(int, input().split()))
# tree = list(map(int, input().split()))

# N = NM[0]
# M = NM[1]

# for H in range(max(tree), 0 , -1):
#     tree_sum = 0
#     for i in range(0,N):
#         if tree[i] - H > 0:
#             tree_sum = (tree[i] - H) + tree_sum

#     if tree_sum == M:
#         print(H)