# import sys
# input = sys.stdin.readline

# N = int(input())
# fibo = [0,1,1]
# for x in range(3,N+1):
#     fibo.append(fibo[x-1] + fibo[x-2])
# print(fibo[N])

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)
arr[1] = 1

if N >= 2:
    for i in range(2,N+1):
        arr[i] = arr[i-1] + arr[i-2]

print(arr[N])