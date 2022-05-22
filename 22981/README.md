# 백준 22981번 휴먼 파이프라인
https://www.acmicpc.net/problem/22981
---

### 문제 해결 날짜
- 2022.05.23
---

### 접근 방식
- V를 정렬한 후 0부터 N-1까지 i로 루프를 돈다.
    * i는 첫번째 팀의 마지막 팀원의 작업속도의 인덱스이다.
    * 작업속도 = `V[0]*(i+1)+V[i+1]*(N-1-i)`를 업데이트한다.
- K%spd==0이 아니면 +1한다.
---

### 소스코드
- 메모리 : 52336 KB
- 시간 : 236 ms
```Python
import sys
from math import ceil
N, K, *V = map(int, sys.stdin.read().split())
V.sort()
spd = 0
for i in range(N-1):
    spd = max(V[0]*(i+1)+V[i+1]*(N-1-i), spd)
print(ceil(K/spd))
```
---

### 오답 노트
- 틀렸습니다.
- 올림을 하는 과정에서 너무 작은 수의 소수부분이 무시된 것 같다.

### 오답 코드
```Python
import sys
from math import ceil
N, K, *V = map(int, sys.stdin.read().split())
V.sort()
spd = 0
for i in range(N-1):
    spd = max(V[0]*(i+1)+V[i+1]*(N-1-i), spd)
print(ceil(K/spd))
```