# 백준 14912번 숫자 빈도수
https://www.acmicpc.net/problem/14912
---

### 문제 해결 날짜
- 2022.04.24
---

### 코드 설명
- 1부터 n까지 d의 개수를 count함수로 센다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 120ms
```Python
import sys
n, d = map(int,sys.stdin.readline().split())
ans = 0
for i in range(1,n+1):
    ans += str(i).count(str(d))
print(ans)
```