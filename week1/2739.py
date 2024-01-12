N = input()
N = int(N)
if N >= 1 and N <= 9:
    for i in range(1, 10):
        if i <= 9:
            print(N, '*' , i , '=' , N * i)
            i += 1
            continue
        else:
            break
else:
    print("1부터 9까지의 정수를 입력해주세요.")
    exit()
