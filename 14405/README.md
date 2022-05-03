# 백준 14405번 피카츄
https://www.acmicpc.net/problem/14405
---

### 문제 해결 날짜
- 2022.05.03
---

### 접근 방식
- 문자열 S는 pi, ka, chu 중 하나로 구성되어야 한다.
- 문자열 S의 정규표현식은 (pi|ka|chu)+이다.
---

### 소스코드
- 메모리 : 33500 KB
- 시간 : 136 ms
```Python
import sys
import re
if re.fullmatch('(pi|ka|chu)+', sys.stdin.readline().strip()):
    print("YES")
else: print("NO")
```