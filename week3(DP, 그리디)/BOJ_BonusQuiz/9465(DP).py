import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int,input().split())))

    if N > 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

    for i in range(2,N):
            arr[0][i] += max(arr[1][i-1],arr[1][i-2])
            arr[1][i] += max(arr[0][i-1],arr[0][i-2])
    print(max(arr[0][N-1] , arr[1][N-1]))
