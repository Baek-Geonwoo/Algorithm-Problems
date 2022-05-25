# 백준 2504번 괄호의 값
https://www.acmicpc.net/problem/2504
---

### 문제 해결 날짜
- 2022.05.25
---

### 코드 설명
- 괄호가 열릴 때 괄호의 종류에 따라 tmp에 2나 3을 곱하고 stack에 추가, 괄호가 닫힐 때 tmp를 2, 3으로 나누어주고 stack에서 pop, 만약 괄호가 `([])같은 경우가 아니라 (), []` 처럼 바로 닫히는 경우 ans에 tmp를 더해준다.
    * 닫는 괄호일 때 스택이 비어있거나 스택의 맨 위의 괄호와 쌍이 맞지 않으면 올바른 괄호열이 아니다.
- 모든 과정이 끝난 후에도 stack에 비어있지 않다면 올바른 괄호열이 아니다.
---

### 소스코드
- 메모리 : 32460 KB
- 시간 : 92 ms
```Python
import sys
from collections import deque
S = sys.stdin.readline().rstrip()
stack = deque()
ans = 0
tmp = 1
dct = {'(':2, '[':3}
for i in range(len(S)):
    if S[i] in '[(':
        stack.append(S[i])
        tmp *= dct[S[i]]
    else:
        if not stack:
            ans = 0
            break
        if S[i] == ')' and stack[-1] == '(':
            if S[i-1] == '(':
                ans += tmp
            stack.pop()
            tmp //= 2
        elif S[i] == ']' and stack[-1] == '[':
            if S[i-1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
        else:
            ans = 0
            break
if stack:
    print(0)
else:
    print(ans)
```