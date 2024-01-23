N = int(input())
binary = {}

for n in range(N):
    par, x, y = input().strip().split()
    binary[par] = [x,y]

def front(par):
    if par != '.':
        print(par, end='')
        front(binary[par][0])
        front(binary[par][1])

def med(par):
    if par != '.':
        med(binary[par][0])
        print(par, end='')
        med(binary[par][1])

def final(par):
    if par != '.':
        final(binary[par][0])
        final(binary[par][1])
        print(par, end='')


front('A')
print()
med('A')
print()
final('A')




# import sys
 
# N = int(sys.stdin.readline().strip())
# tree = {}
 
# for n in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]
 
 
# def preorder(root):
#     if root != '.':
#         print(root, end='')  # root
#         preorder(tree[root][0])  # left
#         preorder(tree[root][1])  # right
 
 
# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])  # left
#         print(root, end='')  # root
#         inorder(tree[root][1])  # right
 
 
# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])  # left
#         postorder(tree[root][1])  # right
#         print(root, end='')  # root
 
 
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')