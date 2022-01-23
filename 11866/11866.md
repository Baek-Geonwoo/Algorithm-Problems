# 백준 11866번 요세푸스 문제 0
https://www.acmicpc.net/problem/11866
---

### 문제 해결 날짜
- 2021.01.23
---

### 접근 방식
- pop, append 연산을 자주 사용하니 queue(deque) 자료구조를 사용한다.
- deque Q에 1부터 n까지의 수를 오름차순으로 저장한다.
- 제일 왼쪽에 있는 요소를 k-1번 append 한 후 popleft하여 그 수를(이 수가 k번째 수 이므로) 큐 Y에 저장하는 것을 Q가 비워질 때까지 반복한다.
---

### 소스코드
- 메모리 : 32288KB
- 시간 : 136ms
```Python
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
```