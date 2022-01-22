# 백준 1991번 문제
https://www.acmicpc.net/problem/1991
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버I
- 2021.12.31
---

### 접근 방식
- D[v] = [l,r]는 v의 왼쪽 자식노드(l)와 오른쪽 자식노드(r)를 순서대로 저장
- preorder(v)는 자기자신(v)을 출력 후 preorder(l)과 preorder(r)을 재귀호출
- inorder(v)는 inorder(l)을 재귀호출 후 자기자신(v)을 출력, inorder(r)을 재귀호출
- postorder(v)는 postorder(l)과 postorder(r)을 재귀호출 후 자기자신(v)을 출력
- l 또는 r이 '.'(없음) 이면 재귀호출하지 않음
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 68ms
```Python
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
```