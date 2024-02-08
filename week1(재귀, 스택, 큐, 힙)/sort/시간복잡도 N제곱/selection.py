def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
# min_idx를 i로 초기화하는 이유는, i까지는 이미 최소값을 반영해서 그렇습니다.
        for j in range(i + 1, len(arr)):
# i+1부터 시작하는 이유는, i까지는 이미 최소값을 반영했기 때문.
            if arr[j] < arr[min_idx]:
                min_idx = j
# j는 계속 순환하면서 최소값을 찾게 되고 최소값이 minidx에 저장됨
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# i와 minidx가 바뀐다. 즉, i는 최소값이 들어갈 위치가 되고 min_idx는 다시 또다른
# 최소값을 찾기 위해 순환하게 된다.

# 선택정렬은 진짜 무식한데 간단한 방법이다.
# 그냥 주어진 리스트에서 최소값을 찾아서 맨 앞으로 보내는 것을 반복하면 된다.
# 즉 넣을 위치는 이미 정해져 있으니 값만 찾으면 된다.
# swap 자체는 한 번만 일어나기 때문에, bubble 정렬보다는 빠르다.
# 시간복잡도 : O(n^2)
# 공간복잡도 : O(n)
