# 백준 2164번 카드2
https://www.acmicpc.net/problem/2164
---

### 문제 해결 날짜
- 2021.01.22
---

### 접근 방식
- ```[1,2,3,4...n]으로 이루어진 리스트를 range로 만들어 Q(deque)에 전달하여 큐를 만든다.
- drop 변수를 스위치로 하여 while문 안에서 해당 요소를 삭제할지 밑으로 보낼지를 설정하여 번갈아가면서 popleft() 연산과 append(popelft()) 연산을 Q의 크기가 1이 될 때까지 반복한다.
---

### 오답노트
- 처음에 리스트가 insert(0,x)를 하면 시간이 오래 걸리기에 시간을 줄이려고 ```[1,2,3,4] 이런 식이 아닌 반대로 [4,3,2,1]``` 이렇게도 해보았으나 시간초과가 나와서 결국 deque를 사용하여 풀었다.
- 각 문제에서 자주 사용하는 연산의 시간복잡도에 맞는 자료구조를 사용해야겠다.

---
### 소스코드
- 메모리 : 49240KB
- 시간 : 344ms
```Python
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
```