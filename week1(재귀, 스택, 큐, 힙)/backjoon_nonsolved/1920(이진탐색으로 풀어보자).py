
N = int(input())
N_array = set(map(int, input().split()))
M = int(input())
M_array = list(map(int, input().split()))


for i in M_array:
    if i in N_array:
        print('1')
    else:
        print('0')

# N = int(input())
# N_array = set(map(int, input().split()))
# M = int(input())
# M_array = list(map(int, input().split()))
# array = list( 0 for _ in range(M))

# for i in range(0,N):
#     for j in range(0,M):
#         if N_array[i] == M_array[j]:
#             array[j] = 1

# for i in range(0,len(array)):
#     print(array[i])