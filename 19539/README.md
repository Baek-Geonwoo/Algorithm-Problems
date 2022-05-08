# 백준 19539번 사과나무
https://www.acmicpc.net/problem/19539
---

### 문제 해결 날짜
- 2022.05.08
---

### 코드 설명
- 각 나무의 희망 높이를 h라 할 때 h//2는 그 나무에 대하여 +2물뿌리개를 사용할 수 있는 횟수이므로 (전체합)/3 <= (+2물뿌리개를 사용가능 횟수)이어야 한다.
---

### 소스코드
- 메모리 : 41620 KB
- 시간 : 96 ms
```Python
import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))
if sum(H)%3 != 0:
    print('NO')
else:
    if sum([h//2 for h in H]) >= sum(H)//3:
        print('YES')
    else:
        print('NO')
```