N = int(input())

A = list(int(input()) for _ in range(N))

for i in range(0,N-1):
    if A[i + 1] < A[i]:
        A[i + 1] = A[i]
        print(A[N-1])