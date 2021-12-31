import sys
input = sys.stdin.readline
def preorder(v):
    l, r = D[v]
    print(v,end='')
    if l != '.':
        preorder(l)
    if r != '.':
        preorder(r)
def inorder(v):
    l, r = D[v]
    if l != '.':
        inorder(l)
    print(v,end='')
    if r != '.':
        inorder(r)
def postorder(v):
    l, r = D[v]
    if l != '.':
        postorder(l)
    if r != '.':
        postorder(r)
    print(v,end='')
n = int(input())
D = {}
for i in range(n):
    p,l,r = input().split()
    D[p] = [l,r]
preorder('A')
print()
inorder('A')
print()
postorder('A')