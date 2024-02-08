import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))


# N = int(input())
# table = [list(map(int, input().split())) for _ in range(N)]
# table.append([0,0,0])

# graph = [[0] * (3) for _ in range(N)]

# rgb = 3
# minimum = min(table[0])
# for i in range(3):
#     if table[0][i] == minimum:
#         rgb = i
#         graph[0][i] = minimum

# value = minimum
# for i in range(1,N):
#     table[i][rgb] = 1e9
#     for j in range(0,3):
#         if table[i][j] == min(table[i][j],table[i][j-1],table[i][j-2]):
#             graph[i][j] = value + table[i][j]
#             rgb = j
#             value = graph[i][j]
#         else:
#             continue

# print(value)