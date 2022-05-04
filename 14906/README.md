# 백준 14906번 스러피
https://www.acmicpc.net/problem/14906
---

### 문제 해결 날짜
- 2022.05.04
---

### 접근 방식
- 스럼프(Slump)는 (D또는 E 다음 F 1개이상 반복)이 반복되고 G로 끝난다.
- 스럼프(Slump)의 정규표현식: ((D|E)F+)+G
- 스림프(Slimp)는 길이 2 이상의 문자열이며 다음과 같은 규칙을 가진다.
    * AH
    * A + B + 스림프(Slimp) + C
    * A + 스럼프(Slump) + C
- 따라서 세번쨰의 경우 A,B,C 부분은 재귀로 스럼프인지 구분하고 스림프의 경우 위의 정규표현식을 이용해 구분한다.
- 스러피(Slurpy)는 스림프(Slimp)+스럼프(Slump)이므로 뒤에서부터 스럼프를 찾은 뒤 나머지 앞 부분으로 스림프인지 구분하여 스러피인지 구분한다.
---

### 소스코드
- 메모리 : 33552 KB
- 시간 : 124 ms
```Python
import sys
import re
def input():
    return sys.stdin.readline().strip()
def Slimp(S):
    if len(S)<2: return 0
    if S[:2] == 'AH' and len(S) == 2:
        return 1
    elif S[0] == 'A' and S[-1] == 'C':
        if S[1] == 'B':
            return Slimp(S[2:-1])
        else:
            return re.fullmatch('((D|E)F+)+G', S[1:-1])
    else: return 0
def SLURPY(S):
    slump = re.search('(((D|E)F+)+G)$', S)
    if slump:
        S = S[:slump.span()[0]]
    else: return 0
    return Slimp(S)

print("SLURPYS OUTPUT")
for _ in range(int(input())):
    if SLURPY(input()):
        print("YES")
    else:
        print("NO")
print("END OF OUTPUT")
```