T = int(input())

for i in range(1, T+1):
    R, S = map(str, input().split())
    R = int(R)
    
    for j in range(len(S)):
        print(S[j] * R, end='')

    print()