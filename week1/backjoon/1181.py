import sys
input = sys.stdin.readline

N = int(input())

eng = []
for _ in range(0,N):
    eng.append(str(input().strip()))

eng = set(eng)
eng = sorted(eng, key= lambda x:(len(x),x))

for i in range(len(eng)):
    print(eng[i])