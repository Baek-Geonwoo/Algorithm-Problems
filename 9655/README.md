# 백준 9655번 문제
https://www.acmicpc.net/problem/9655
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2021.01.17
---

### 접근 방식
- 상근이와 창영이 모두 돌을 홀수 개씩 가져가기 때문에 n이 홀수이면 상근이가 이기고 n이 짝수이면 창영이가 이긴다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
n = int(sys.stdin.readline())
if n%2:
    print("SK")
else:
    print("CY")
```