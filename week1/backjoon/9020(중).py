T = int(input())
n = [int(input()) for _ in range(T)]

# n0 = 8

notsosu = []
for i in range(0,T-1):
    num = n[i]
    temp = []
    for j in range(n[T-1]-1):
        if j > 0:
            for k in range(2, j):
                if j % k == 0:
                    temp.append(j)
    notsosu.append(temp)

nau = list(range(1,n[T-1] - 1))
sosu = list(set(nau) - set(sum(notsosu, [])))
sosu.sort()

for ai in range(T):
    min_diff = abs(n[ai] - 2 * sosu[0])  # 초기값을 첫 번째 소수와의 차이로 설정
    selected_values = (sosu[0], n[ai] - sosu[0])

    for a in range(1, len(sosu)):
        if n[ai] - sosu[a] in sosu:
            diff = abs(n[ai] - 2 * sosu[a])

            if diff < min_diff:
                min_diff = diff
                selected_values = (sosu[a], n[ai] - sosu[a])

    if selected_values:
        print(selected_values[0], selected_values[1])

#답안
#         import math

    # def d(N): # 소수 판별 함수
    #     if N == 1:
    #         return False
    #     for i in range(2, int(math.sqrt(N))+1):
    #         if N % i == 0:
    #             return False
    #     return True
    
    # N = int(input()) # 테스트 케이스 수 입력

    # for _ in range(N):
    #     num = int(input()) # 짝수 입력
        
    #     A = num // 2 # 두 수 중 줄어드는 변수
    #     B = num // 2 # 두 수 중 늘어나는 변수
        
    #     for _ in range(num // 2):
    #         if d(A) and d(B): # 두 수가 소수이면 출력
    #             print(A, B)
    #             break
    #         else: # 소수가 아니면 두 수를 줄이고 늘리기
    #             A -= 1
    #             B += 1