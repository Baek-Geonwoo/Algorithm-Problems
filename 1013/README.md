# 백준 1013번 Contact
https://www.acmicpc.net/problem/1013
---

## 문제 해결 날짜
- 2021.03.29
---

## 풀이1 - 조건문

### 코드 설명
- 겉의 while문의 시작위치(i)는 항상 100+1+ 또는 01의 패턴이다.
- i부터 시작하여 00 또는 11인 경우 'NO'리턴
- 01인 경우 continue
- 10인 경우 그 다음이 0인 것을 확인한 후, i < n이고 ```S[i] == '0'```인 동안 while루프를 돌면서 0을 계속 skip한다. 그 다음 1이 1개 이상 나온 것을 확인한 후(1이 없으면 'NO' 리턴) i < n이고 ```S[i] == '1'```인 동안 while루프를 돌면서 1을 계속 skip한다.(패턴 만족)
    * 이때, i < n-1이면 ```S[i+1] == '1'```인 경우 ...101이므로 패턴을 만족하여 i 업데이트, 아니면 ```S[i]```뒤에 0이 2개 이상 나오는 경우이므로 ```S[i-1] == S[i-2] == '1'```이면 i -= 1한다.(100+1+ 패턴 뒤에 바로 다시 100+1+패턴이 나올 수 있으므로)
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
def wave(S):
    n = len(S)
    i = 0
    while i < n:
        if i == n-1 or S[i] == S[i+1]:
            return 'NO'
        i += 2
        if S[i-2] == '0':
            continue
        if i >= n or S[i] != '0':
            return 'NO'
        i += 1
        while i<n and S[i] == '0':
            i += 1
        if i == n:
            return 'NO'
        while i<n and S[i] == '1':
            i += 1
        if i < n-1:
            if S[i+1] == '1':
                i += 2
            else:
                if S[i-1] == S[i-2] == '1':
                    i -= 1
    return 'YES'

for _ in range(int(I())):
    print(wave(I().strip()))
```
---

## 풀이2 - DFA

### 코드 설명
- 정규표현식 (100+1+|01)+에 대한 NFA를 그린 후 그를 토대로 DFA를 그려 입력받은 문자열이 DFA의 정답노드에서 끝나는지 확인한다.
- 아래는 (100+1+|01)+을 NFA, DFA로 나타낸 것이다.
- [README.md](https://github.com/Baek-Geonwoo/Algorithm-Problems/files/8370570/README.md)
- 정규표현식 (100+1+|01)+을 표현한 NFA에서 정답노드는 2,6이고, DFA에서는 2,6,7이다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
dfa = ((1,3),
    (None,2),
    (1,3),
    (4,None),
    (5,None),
    (5,6),
    (1,7),
    (8,7),
    (5,2)
)

def wave(i, n):
    if i == len(S):
        return n in (2,6,7)
    if dfa[n][int(S[i])] != None:
        return wave(i+1,dfa[n][int(S[i])])
        
for _ in range(int(I())):
    S = I().strip()
    print('YES') if wave(0,0) else print('NO')
```
---

## 풀이3 - 정규표현식

### 코드 설명
- re 라이브러리를 활용해서 입력받은 문자열이 정규표현식 (100+1+|01)+에 해당하는지 출력한다. (match가 아닌 fullmatch를 사용하는 이유는 입력받은 문자열 전체가 위의 정규식에 해당해야 하기 때문이다.)
---

### 소스코드
- 메모리 : 33468KB
- 시간 : 128ms
```Python
import sys, re
I = sys.stdin.readline
for _ in range(int(I())):
    print('YES') if re.fullmatch('(100+1+|01)+',I().strip()) else print('NO')
```
