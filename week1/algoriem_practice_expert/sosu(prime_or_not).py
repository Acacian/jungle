# 내 연습용 답안
import math

def issosu(N):
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(N))+1):
        if is_prime[i]:
            for j in range(i * i, N + 1 , i):
                is_prime[j] = False

    primes = [num for num in range(2, N + 1) if is_prime[num]]
    return primes

N = 15
print(issosu(N))


## 소수를 푸는 방법은 하나의 def에는 소수를 구별하는 함수를,
## 다른 하나에는 1~N까지 소수를 불러오게만 하면 된다.

# import math

# def isPrime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# def solution(n):
#     answer = 0
#     for i in range(2, n+1):
#         if isPrime(i) == True:
#             answer += 1
#     return answer

# 아래는 에리스토텔레스의 체 사용
# n = 8

# def solution(n):
#     answer=0
#     # 1. 배열을 생성하여 값을 초기화 한다. 모든 수가 소수(True)인 것으로 초기화,
#     array=[True for i in range(n+1)]
    
#     # 약수의 성질에 따라 가운데 약수(제곱근)까지만 확인해도 됨
#     for i in range(2,int(n**(1/2))+1):
#         if array[i]==True: # i가 소수인 경우
#         	# 2. 특정 숫자의 배수에 해당하는 숫자들을 지운다. (i를 제외한 모든 배수를 지우기)
#             j = 2
#             while i * j <= n:
#             	# 배수들을 지워주는 과정
#                 array[i*j] = False
#                 j += 1
#     # 4. 남아있는 숫자들(True값인 것들만) 개수를 세준다.
#     for i in range(2,n+1):
#         if array[i]:
#             answer+=1
#     return answer

# result = solution(n)
# print(result)