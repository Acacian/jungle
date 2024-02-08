# 부모 노드 >= 자식 노드 : 최대 힙 / 반대의 경우 최소 힙으로 구분
# 힙은 완전 이진 트리이므로 배열로 표현 가능

# 새로운 노드가 힙의 가장 마지막에 들어가고, 이후 비교를 통해 위치 변경.
# 만약 노드를 삭제 시 루트 노드를 삭제하고, 가장 마지막 노드를
# 루트 노드로 옮긴 후 비교를 통해 위치 변경.

# 자식 노드로 내려갈 때마다 2배씩 증가하므로 O(log N)의 시간 복잡도를 가진다.
# 추가적인 배열이 필요하지 않아 메모리 측면에서 병합보단 효율적이고,
# 항상 O(N log N)의 시간 복잡도를 가지기 때문에 시간 복잡도 면에서 퀵보다 효율적이다
# 퀵 정렬은 최악의 경우 O(N^2)의 시간 복잡도를 가지기 때문에..

# 힙 정렬
# 이건 최대 힙

def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  # 왼쪽 자식 노드와 오른쪽 자식 노드의 인덱스를 구함
  # 2진법으로 늘어나기때문
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    # 왼쪽 자식 노드가 존재하고, 현재까지 가장 큰 값보다 크다면 largest를 업데이트
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    # 오른쪽 자식 노드가 존재하고, 현재까지 가장 큰 값보다 크다면 largest를 업데이트
    
  if largest != index: #이 조건일 때 계속 순환하게 된다.
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

# 7,2,5부터 검색
# 그림을 그린다면 오른쪽 맨 밑부터 시작하게됨.