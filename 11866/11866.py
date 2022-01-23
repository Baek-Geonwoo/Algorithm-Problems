import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
Q = deque(range(1,n+1))
Y = deque() # (n,k) 요세푸스 수열을 저장할 큐
while Q:
    for _ in range(k-1):
        Q.append(Q.popleft())
    Y.append(Q.popleft())
print('<'+", ".join(map(str,Y))+'>')