# 백준 2872번 우리집엔 도서관이 있어
https://www.acmicpc.net/problem/2872
---

### 문제 해결 날짜
- 2021.01.26
---

### 접근 방식
- 그리디 기준 : 오름차순이 아닌 가장 큰 수를 찾는다.
- 책의 번호들이 적힌 리스트 L에서 뒤(인덱스 N-1)부터 앞 방향으로 오름차순으로 정렬되어 있지 않은 가장 큰 수(m)를 찾는다. 예를 들어 ```L = [3, 4, 2, 1, 5]```이면 m은 2이다. 
---

### 소스코드
- 메모리 : 42616KB
- 시간 : 196ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
L = [int(I()) for _ in range(N)]
m = N
#오름차순 아닌 가장 큰 수
for i in range(N-1,-1,-1):
    if L[i] == m:
        m -= 1
print(m)
```
---
### 오답노트
- 오름차순 정렬되었을 때와 비교해 오름차순 정렬되었을 때의 그 수의 자리에 없는 최댓값을 구한 것이지만 그 경우 3 4 2 1 5 같은 경우 3은 움직일 필요가 없는데도 4가 제 자리에 있지 않아 오답이 되었다.

### 오답코드
```Python
import sys
I = sys.stdin.readline
N = int(I())
L = [int(I()) for _ in range(N)]
m = 0
for i in range(N):
    if L[i] != i+1:
        m = max(m,L[i])
print(m-1)
```