# 백준 2671번 잠수함식별
https://www.acmicpc.net/problem/2671
---

## 문제 해결 날짜
- 2021.03.31
---

## 풀이1 - DFA

### 코드 설명
- 정규표현식 (100+1+|01)+에 대한 NFA를 그린 후 그를 토대로 DFA를 그려 입력받은 문자열이 DFA의 정답노드에서 끝나는지 확인한다.
- 아래는 (100+1+|01)+을 NFA, DFA로 나타낸 것이다.
![NFA, DFA](https://user-images.githubusercontent.com/86524230/160595434-baa4a56c-a93e-441c-bf96-fd124f907511.jpg)
- 정규표현식 (100+1+|01)+을 표현한 NFA에서 정답노드는 2,6이고, DFA에서는 2,6,7이다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
dfa = (
    (1,3),
    (None,2),
    (1,3),
    (4,None),
    (5,None),
    (5,6),
    (1,6),
)
def solve(i,n):
    if i == len(S):
        return n in (2,6)
    if dfa[n][int(S[i])] != None:
        return solve(i+1, dfa[n][int(S[i])])
S = sys.stdin.readline().strip()
print("SUBMARINE") if solve(0,0) else print("NOISE")
```
---

## 풀이2 - 정규표현식

### 코드 설명
- 문자열의 모든 부분이 정규표현식 (100+1+|01)+을 따라야 하므로 re.fullmatch를 사용한다.
---

### 소스코드
- 메모리 : 33468KB
- 시간 : 124ms
```Python
import sys, re
print("SUBMARINE") if re.fullmatch('(100+1+|01)+',sys.stdin.readline().strip()) else print("NOISE")
```