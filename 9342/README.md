# 백준 9342번 염색체
https://www.acmicpc.net/problem/9342
---

### 문제 해결 날짜
- 2022.05.06
---

### 코드 설명
- 염색체 규칙:
    * 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
    * 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
    * 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
    * 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
    * 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
- 따라서 이 염색체의 정규표현식은 `[A-F]{0,1}A+F+C+[A-F]{0,1}`이다.
---

### 소스코드
- 메모리 : 33496 KB
- 시간 : 124 ms
```Python
import sys
import re
def input():
    return sys.stdin.readline().strip()
def DNA(S):
    return re.fullmatch('[A-F]{0,1}A+F+C+[A-F]{0,1}', S)
for _ in range(int(input())):
    if DNA(input()):
        print("Infected!")
    else:
        print("Good")
```