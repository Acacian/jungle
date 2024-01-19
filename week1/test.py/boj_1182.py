import sys
input = sys.stdin.readline

array = list(map(int, input().split()))
N = array[0]
S = array[1]
numbers = list(map(int, input().split()))
count = 0
stack = []

for i in range(1, pow(2, N)): # 이건 무조건 2의 N승이므로 짝수니까
    for j in range(N):
        if (i // pow(2, j)) % 2 == 1: # 홀짝 검사
            stack.append(numbers[j])
    if sum(stack) == S:
        count += 1
    stack = []
print(count)


# if (i // pow(2, j)) % 2 == 1: 조건은 이진수 표현을 이용하여 부분집합을 만들 때 사용됩니다. 이 코드는 길이가 N인 배열 numbers에서 모든 가능한 부분집합 중에서 원소의 합이 S와 일치하는 부분집합의 개수를 찾는 것입니다.

# 여기서 i는 1부터 2^N-1까지의 수를 나타내며, 각 수 i는 N자리 이진수로 표현됩니다. j는 numbers 배열의 인덱스를 나타내며, i // pow(2, j)를 통해 이진수에서 특정 자리의 값을 확인합니다.

# if (i // pow(2, j)) % 2 == 1:의 조건은 이진수에서 특정 자리의 값이 1인 경우를 검사하고 있습니다. 이는 i를 2진수로 나타냈을 때, j번째 자리의 비트가 1인지를 확인하는 것입니다.

# 이 조건은 현재의 부분집합을 만들 때 numbers[j]를 포함할지 여부를 결정하는데 사용됩니다. 만약 j번째 자리의 비트가 1이면, 해당 인덱스의 numbers 배열의 값이 현재 부분집합에 추가됩니다. 이렇게 만들어진 부분집합의 합이 S와 일치하는지 확인하여 count를 증가시킵니다.

# 즉, if (i // pow(2, j)) % 2 == 1:는 현재 부분집합에 numbers[j]를 포함할지 여부를 결정하는데 사용되는 조건입니다.