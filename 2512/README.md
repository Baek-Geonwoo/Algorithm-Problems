# 백준 2512번 예산
https://www.acmicpc.net/problem/2512
---

### 문제 해결 날짜
- 2021.03.07
---

### 코드 설명
- 모든 요청이 배정될 수 있는 경우 가장 높은 예산을 요청한 지방의 예산을 출력한다.(아래는 그렇지 않은 경우에 대한 코드 설명이다.)
- m은 각 지방에 재정할 수 있는 예산의 상한선이다.
- 각 지방의 예산을 a라하면 min(m,a)의 합을 Sum이라 할 때 다음과 같이 실행한다.
    * Sum <= M 이면 m을 더 증가시킬 수 있다는 것이므로 low를 m+1로 증가시킨다.
    * Sum > M 이면 m일 때 예산이 초과된다는 것이므로 high를 m-1로 감소시킨다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 100ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
A = [int(e) for e in I().split()]
M = int(I())
if sum(A) <= M:
    print(max(A))
else:
    low, high = 1, max(A)
    while low <= high:
        m = (low + high)//2
        Sum = sum([min(m,a) for a in A])
        if Sum <= M:
            low = m+1
        else:
            high = m-1
    print(high)
```