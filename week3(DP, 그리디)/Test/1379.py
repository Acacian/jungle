import sys
input = sys.stdin.readline

N = int(input())
arr = [[0,0,0]]

for _ in range(N):
    arr.append(list(map(int, input().split())))

first = sorted(arr , key = lambda x: [x[1]])
second = sorted(arr , key = lambda x: [x[2]])

count = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        if first[i][2] <= first[j][1]:
            count += 1
            break

print(count)