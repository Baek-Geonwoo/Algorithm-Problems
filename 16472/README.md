# 백준 16472번 고냥이
https://www.acmicpc.net/problem/16472
---

### 문제 해결 날짜
- 2022.05.07
---

### 접근 방식
- s, e는 각각 문자열의 부분의 시작과 끝 인덱스이다.
- kind는 `S[s:e+1] -> 부분 문자열이라 한다.`의 각각의 알파벳 개수를 저장한 딕셔너리이다.
- s, e < L인동안 다음을 반복한다.
    * 부분 문자열의 알파벳 종류(kind)가 N이하이면 인식이 가능하므로 ans = max(ans, e-s)
    * N 초과이면 인식이 불가능하므로 len(kind)(부분문자열의 알파벳 종류)가 N이하가 될 때까지 s += 1 하며 kind를 update 한다.
    * e += 1
---

### 소스코드
- 메모리 : 32432 KB
- 시간 : 192 ms
```Python
import sys
from collections import defaultdict
N, S = sys.stdin.read().split()
N = int(N)
s, e = 0, 0
ans, L = 1, len(S)
kind = defaultdict(int)
while s<L and e<L:
    kind[S[e]] += 1
    if N >= len(kind):
        ans = max(ans, e-s+1)
    else:
        while s<=e and len(kind)>N:
            if kind[S[s]]:
                kind[S[s]] -= 1
            if not kind[S[s]]:
                kind.pop(S[s])
            s += 1
    e += 1
print(ans)
```
---

### 오답 노트
- 시간 초과
- kind를 구할 때 부분문자열을 슬라이싱해서 시간복잡도가 O(L^2)이 되어 시간초과되었다.

### 오답 코드
```Python
import sys
N, S = sys.stdin.read().split()
N = int(N)
s, e = 0, 0
ans, L = 0, len(S)
while e<L and s<=e:
    kind = len(set(S[s:e+1]))
    if N >= kind:
        e += 1
        ans = max(ans, e-s)
    else:
        s += 1
print(ans)
```