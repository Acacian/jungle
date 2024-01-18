import sys
input = sys.stdin.readline

array = list(map(int, input().split()))
N = array[0]
S = array[1]
numbers = list(map(int, input().split()))
count = 0
stack = []

for i in range(1, pow(2, N)):
    for j in range(N):
        if (i // pow(2, j)) % 2 == 1:
            stack.append(numbers[j])
    if sum(stack) == S:
        count += 1
    stack = []
print(count)