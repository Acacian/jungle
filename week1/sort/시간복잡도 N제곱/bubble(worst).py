def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
# end는 정렬이 끝나는 시점을 알려주며, 0이 되면 그만둔다.
        last_swap = 0
# 계속 last_swap을 0으로 초기화시키고 다시 아래의 반복을 시작한다.
        for i in range(end):
            if arr[i] > arr[i + 1]:
# 비교비교
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
# 만약 i가 i+1보다 크면 swap을 해 준다. 그리고 swap수는 lastswap에 저장된다.
                last_swap = i
        end = last_swap
# 이걸 end에 넣고 end가 0이 될 때까지 한무반복 ㄱㄱ

# 기본적으로 bubble은 맨 앞에서부터 정렬이 되어있는지 확인하면서 정렬을 진행한다.
# 정렬할 때 i와 그 다음 i와 비교하게 된다.
# i가 i+1보다 크면 swap을 해 주고, swap 한 횟수를 last_swap에 저장한다.
# 그렇게 한 사이클을 돌면 맨 뒤에는 가장 큰 수가 위치하게 되고, 다시 처음부터 정렬을 시작한다.
# 선택정렬과 마찬가지로, 정렬이 끝나는 시점은 swap이 일어나지 않을 때이다.
        
# 이 때, 처음부터 정렬을 시작하는 것이 아니라, last_swap까지만 정렬을 시작한다.
# 왜냐하면, last_swap 이후에는 이미 정렬이 되어있기 때문이다.
# 이는 기본세팅은 아니고 최적화된 버블 정렬이다.