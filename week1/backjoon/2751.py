import sys
input=sys.stdin.readline


N = int(input())
num = []
for _ in range(1,N+1):
    num.append(int(input()))

num = sorted(num)
for i in range(len(num)):
    print(num[i])