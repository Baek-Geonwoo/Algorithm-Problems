# 백준 1174번 줄어드는 수
https://www.acmicpc.net/problem/1174
---

### 문제 해결 날짜
- 2021.02.11
---

### 코드 설명
- ```0~9까지 숫자들 중에 중복 없이 1~10개를 뽑는 것이므로 총 경우의 수는 10C1+10C2...+10C10=2^10-1=1023이다.```즉, combination을 사용해서 전부 구한 후 N번째 줄어드는 수를 구해도 무방하다.
- C에 i가 1부터 10까지 combinations(range(10),i)안의 리스트들을 c라 하면 c를 정렬하여 정수로 바꿔준 다음 C에 append한다.
- ```C[N-1]을 출력하는데 C[N-1]이 없으면 오류가 발생하며 try-except로 -1을 출력한다.```
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
from itertools import combinations
N = int(sys.stdin.readline())
C = []
for i in range(1,11):
    for c in combinations(range(10), i):
        temp = sorted(c)
        I, d = 0, 1
        for t in temp:
            I += t*d
            d *= 10
        C.append(I)
C.sort()
try:
    print(C[N-1])
except:
    print(-1)
```