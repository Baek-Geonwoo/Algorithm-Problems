# 백준 2075번 N번째 큰 수
https://www.acmicpc.net/problem/2075
---

### 문제 해결 날짜
- 2022.04.06
---

### 코드 설명
- 메모리 제한이 12MB밖에 되지 않으므로 heap의 크기를 N으로 유지한다.
- 처음 1줄을 min-heap인 H에 저장하고 heapify한다.
- H에 현재까지 가장 큰 N개의 수만 저장되도록 입력받은 줄의 수(a)들을 순회하면서 ```H[0]<a이면 heappushpop(H,a)하여 a를 heap에 push하고 a보다 작은 수를 pop한다.```
- H의 크기는 항상 N으로 유지되고, H는 min-heap이므로 ```H[0]이 N번째 큰 수이다.```
---

### 소스코드
- 메모리 : 32928KB
- 시간 : 884ms
```Python
import sys, heapq
I = sys.stdin.readline
N = int(I())
H = list(map(int,I().split()))
heapq.heapify(H)
for _ in range(N-1):
    A = map(int,I().split())
    for a in A:
        if H[0] < a:
            heapq.heappushpop(H,a)
print(H[0])
```