# 백준 2729번 이진수 덧셈
https://www.acmicpc.net/problem/2729
---

### 문제 해결 날짜
- 2022.04.27
---

### 접근 방식
- 2진수를 10진수로 바꾸어 더한 뒤 다시 2진수로 변환해 출력한다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 64ms
```Python
import sys
input = sys.stdin.readline
def B(x):
    return int(x,2)
T = int(input())
for _ in range(T):
    a, b = map(B,input().split())
    print(format(a+b,'b'))
```