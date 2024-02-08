import sys
input = sys.stdin.readline

N = int(input())
F = N // 10
B = N % 10
count = 0


while True:
    sum = F + B
    F = B
    B = sum % 10
    count += 1
    if F * 10 + B == N:
        break
print(count)