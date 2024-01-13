num = 0
max = 0

for i in range(1,10):
    n = input()
    n = int(n)
    if n > max :
        max = n
        num = i

print(max)
print(num)