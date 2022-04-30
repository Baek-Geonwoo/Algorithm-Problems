# 백준 1759번 암호 만들기
https://www.acmicpc.net/problem/1759
---

### 문제 해결 날짜
- 2022.04.30
---

### 코드 설명
- A에 C개의 문자들을 입력받아 사전순으로(오름차순) 정렬한다.
- solution(i,S)는 길이 L의 암호 후보를 만드는 함수로 S(암호 후보)의 길이가 L이 되면 check(S)가 참이면 S를 출력한 뒤 재귀를 종료
    * check(S)는 S에 모음이 1개이상, 자음이 2개 이상인지 확인하는 함수
- i는 A에서의 인덱스로 i == C가 되어도 재귀를 종료한다.
- 사전순으로 가능한 암호들을 출력해야 하기 때문에 `solution(i+1,S+A[i])`를 먼저 재귀호출하고 그 다음에 solution(i+1,S)를 재귀호출한다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 80ms
```Python
import sys
def in_vowel(S):
    for v in "aeiou":
        if v in S:
            return True
    return False
def solution(i,S):
    if len(S) == L:
        if in_vowel(S):
            print(S)
        return
    if i == C: return
    solution(i+1,S+A[i])
    solution(i+1,S)

L, C, *A = sys.stdin.read().split()
L, C = int(L), int(C)
A.sort()
solution(0,"")
```