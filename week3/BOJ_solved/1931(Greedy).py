#2회차
n = int(input())
time = []

for _ in range(n):
    x , y = map(int, input().split())
    time.append([x,y])

time = sorted(time, key = lambda x :(x[1],x[0]))
dv = time[0][1]

count = 1
for i in range(1,n):
    if time[i][0] >= dv:
        count += 1
        dv = time[i][1]
print(count)













# n = int(input())
# time = []
# for i in range(n):
#     start, end = map(int, input().split())
#     time.append([start, end])

# time=sorted(time, key=lambda x: (x[1],x[0])) # 회의가 끝나는 시간으로 오름차순 정렬 후 시작 시간이 빠른 것으로 오름차순 정렬

# count = 1
# end_time = time[0][1]
# for i in range(1,n):
#     if time[i][0] >= end_time:
#         count+=1
#         end_time = time[i][1]

# print(count)