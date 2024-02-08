import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

for k in range(3,N+1):
    arr[k] = (arr[k-1] + arr[k-2]) % 15746
print(arr[N])