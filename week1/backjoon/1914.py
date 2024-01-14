def hanoi_tower(n, start, end) :
    if n == 1 :
        # print("마지막", n)
        print(start, end)
        return     
    # print(int(n) , start, end, "원반이동1")
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    # print(int(n), start, end , "원반이동2")
    print(start, end) # 2단계
    # print(n , start, end, "원반이동3")
    hanoi_tower(n-1, 6-start-end, end) # 3단계

    # else:     << 같은뜻
    #     hanoi_tower(n-1, start, 6-start-end) # 1단계
    #     print(start, end) # 2단계
    #     hanoi_tower(n-1, 6-start-end, end) # 3단계

n = int(input())
print(2**n-1)
#여기 if부분
if n <= 20 :
    hanoi_tower(n, 1, 3)