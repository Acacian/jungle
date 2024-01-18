import sys
import heapq

input = sys.stdin.readline

N = int(input())
min_heap = []
max_heap = []

for _ in range(N):
    num = int(input())
    # 넘어가면서 최대값과 최소값이 같다면 최대힙에 넣어준다.(일단 넣는거)
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, num)
    #(mix heap의 최소값이(절대값이라 -로 치환되어서 값은 같음) max heap의 최대값보다 크다면 swap)
    if min_heap and max_heap[0][1] > min_heap[0]:
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, temp_max)

    print(max_heap[0][1])
