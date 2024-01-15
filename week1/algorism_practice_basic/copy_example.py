import copy

x = [[1,2,3],[4,5,6]]
y = x.copy()
x[0][1] = 9
print(x)
print(y)

xx = [[1,2,3],[4,5,6]]
z = copy.deepcopy(xx)
xx[0][1] = 9
print(xx)
print(z)
# deepcopy는 copy의 원래 개체 영향을 안 받음.