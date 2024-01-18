N = str(input())
new = ''
cnt = 0

while N != new:
    # 처음으로 돌리는데
    if cnt == 0:
        # 0보다 작다면
        if int(N) < 10:
            # 0을 붙여 두자리 수 만들기
            new = str(N) + str(N)
            print('new >', new)
            cnt += 1
        # 10보다 크거나 같다면
        else:
            # 각 자리수의 합
            sum = str(int(N[0]) + int(N[1]))
            new = str(N[1]) + str(sum[-1])
            cnt += 1
    # 두번째 이상으로 돌리는데
    else:
        # 각 자리수의 합
        sum = str(int(new[0]) + int(new[1]))
        new = str(new[1]) + str(sum[-1])
        print('########### 거기 지점 ###########')
        print('new >', new)
        cnt += 1

print(cnt)