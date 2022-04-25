# 백준 12755번 수면 장애
https://www.acmicpc.net/problem/12755
---

### 문제 해결 날짜
- 2022.04.25
---

### 접근 방식
- i부터 시작해서 1씩 증가해가며 n이 N이 될떄까지 i를 증가시킨다.
- n == N이면 str(i)에서 전체의 N번째 숫자인 j를 출력하고 종료한다.
---

### 소스코드
- 메모리 : 114976KB
- 시간 : 1168ms
```Python
import sys
N = int(sys.stdin.readline())
i = 1
n = 0
while True:
    s = str(i)
    for j in s:
        n += 1
        if n == N:
            print(j)
            sys.exit()
    i += 1
```