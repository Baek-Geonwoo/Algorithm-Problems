# 백준 10825번 국영수
https://www.acmicpc.net/problem/10825
---

### 문제 해결 날짜
- 2021.03.20
---

### 코드 설명
- sort함수에서 -국어, 영어, -수학, 이름 순으로 정렬한다.
---

### 소스코드
- 메모리 : 62900KB
- 시간 : 480ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
A = []
for _ in range(N):
    name, *score = I().split()
    A.append([name] + list(map(int,score)))
A.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for a in A:
    print(a[0])
```