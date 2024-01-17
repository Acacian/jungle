import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)

## 내 답대로 해도 되기는 하는데 heapq 모듈을 써보자

# import sys
# input = sys.stdin.readline

# N = int(input())
# ex = [int(input()) for _ in range(N)]
# array = []

# for i in range(0,len(ex)):
#     if ex[i] == 0:
#         if len(array) == 0 or max(array) == 0:
#             print(0)
#         else:
#             print(max(array))
#             array.remove(max(array))
#     else:
#         array.append(ex[i])