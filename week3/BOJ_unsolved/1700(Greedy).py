N , K = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)

count = 0
for i in range(len(arr)):
    if arr[i] != arr[i-1]:
        count += 1
if count - N >= 0:
    answer = count - N
else:
    answer = 0

print(answer)

N, K = map(int, input().split())

multap = [0] * N
li = list(map(int, input().split()))
res = swap = num = max_I = 0

for i in li:
    # 이미 i가 멀티탭에 끼워져 있다면
    if i in multap:
        pass
    # 멀티탭에 빈 칸이 있다면 0인 곳에 배정
    elif 0 in multap:
        multap[multap.index(0)] = i
    # i가 멀티탭에 안 끼워져 있고 빈 칸도 없는 상황
    else:
        for j in multap: # 멀티탭을 쭉 스캔
            if j not in li[num:]: # num부터 쭉 스캔 => 처음에는 num == 0 => for 문 한바꾸 돌 떄마다 스캔 위치를 위로 올려
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)
