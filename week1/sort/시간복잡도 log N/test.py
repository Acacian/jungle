def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  # 왼쪽 자식 노드와 오른쪽 자식 노드의 인덱스를 구함
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    # 왼쪽 자식 노드가 존재하고, 현재까지 가장 큰 값보다 크다면 largest를 업데이트
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    # 오른쪽 자식 노드가 존재하고, 현재까지 가장 큰 값보다 크다면 largest를 업데이트
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)
    # largest가 index와 다르다면, 현재 노드와 largest를 교환하고 재귀적으로 heapify를
    # 호출하여 서브트리를 최대 힙으로 만듦

def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    # 힙을 구성(루트까지 heapify를 호출 - 중간부터 시작)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)
    # 비교하면서 가장 큰 값을 맨 뒤로 보냄

  return unsorted

unsorted_list = [4, 1, 7, 3, 9, 2, 5]
print("정렬 전 리스트:", unsorted_list)

# 힙 정렬 함수 호출
sorted_list = heap_sort(unsorted_list)
print("정렬 후 리스트:", sorted_list)