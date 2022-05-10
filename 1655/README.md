# 백준 1655번 가운데를 말해요
https://www.acmicpc.net/problem/1655
---

### 문제 해결 날짜
- 2022.05.10
---

### 코드 설명
- 중간값을 기준으로 작은 값들이 힙 S에 들어가고 큰 값들이 힙 B에 들어간다.
- S는 max heap, B는 min heap으로 구현
- 두 힙의 크기가 같으면 새로운 값을 S에 추가하고 아니면 B에 새로운 값을 추가한다.
- S와 B의 루트를 비교해서 S의 루트가 더 클 경우 둘을 바꾼다.
- 길이가 같을 경우 중간의 두 수 중 작은 수를 출력하므로 항상 S의 루트를 출력한다.
---

### 소스코드
- 메모리 : 36416KB
- 시간 : 288ms
```Python
import sys
from heapq import *
S = []
B = []
def input():
    return int(sys.stdin.readline())
N = input()
for _ in range(N):
    if len(S) == len(B):
        heappush(S,-input())
    else:
        heappush(B,input())
    if len(B) != 0 and -S[0] > B[0]:
        b = -heappop(S)
        s = -heappop(B)
        heappush(S,s)
        heappush(B,b)
    print(-S[0])
```