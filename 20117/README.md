# 백준 20117번 호반우 상인의 이상한 품질 계산법
https://www.acmicpc.net/problem/20117
---

### 문제 해결 날짜
- 2022.04.10
---

### 코드 설명
- 호반우를 2마리(A에서 현재 최소, 최대)씩 묶으면 중간값이 최댓값으로 나오므로 이익이 최대가 된다. 호반우가 홀수의 경우 가운데에 있는 한마리는 따로 판다.
- A를 입력받아 정렬한 후 deque에 넣고 N이 홀수인 경우 가운데 한마리를 제거하여 그 품질을 ans에 더하고 그 다음부터 A가 빌 때까지 왼쪽, 오른쪽에서 pop한 뒤 오른쪽에서 pop된 값에 2를 곱하여 ans에 더한다.
---

### 소스코드
- 메모리 : 40940KB
- 시간 : 132ms
```Python
import sys
from collections import deque
N, *A = map(int, sys.stdin.read().split())
A = deque(sorted(A))
ans = 0
if N%2:
    ans += A[N//2]
    A.remove(A[N//2])
while A:
    A.popleft()
    ans += A.pop()*2
print(ans)
```