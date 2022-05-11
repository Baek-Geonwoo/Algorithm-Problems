# 백준 1662번 압축
https://www.acmicpc.net/problem/1662
---

### 문제 해결 날짜
- 2022.05.11
---

### 코드 설명
- (를 만나면 stack에 K와 현재까지 압축을 푼 문자열을 저장한다.
- )를 만나면 stack에서 pop하여 현재까지의 `문자열*K+스택에 저장된 문자열 길이`한다.
- 숫자를 만나면 K에 그 숫자를 정수형으로 저장하고 현재 문자열 길이를 1 증가시킨다.
---

### 소스코드
- 메모리 : 32416KB
- 시간 : 92ms
```Python
import sys
from collections import deque
S = sys.stdin.readline().rstrip()
stack = deque()
ans = 0
for s in S:
    if s == '(':
        stack.append((K,ans-1))
        ans = 0
    elif s == ')':
        K, prev = stack.pop()
        ans = K*ans+prev
    else:
        K = int(s)
        ans += 1
print(ans)
```