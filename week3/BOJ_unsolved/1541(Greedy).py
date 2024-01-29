#2회차





















import sys
input = sys.stdin.readline

PB = list(input().rstrip().split('-'))
s = 0

for i in PB[0].split('+'):
    s += int(i)
for i in PB[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)