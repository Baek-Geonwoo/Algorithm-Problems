import sys
from collections import deque
n = int(sys.stdin.readline())
Q = deque(e for e in range(1,n+1))
drop = True #버릴지 아래로 옮길지 저장하는 변수
while len(Q) != 1:
    if drop:
        Q.popleft()
        drop = False
    else:
        Q.append(Q.popleft())
        drop = True
print(Q[0])