# 백준 2204번 문제
https://www.acmicpc.net/problem/2204
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2021.01.10
---

### 접근 방식
- w에 사전상 가장 앞서는 단어를 저장
- curr에 단어를 입력받고 w와 curr을 lower()함수를 이용해 대소문자 구분 없이 w와 curr를 비교, 사전순으로 더 앞에 있는 단어를 w에 저장
- 리스트에 저장하는 방법도 있지만 메모리 사용을 줄이기 위해 w에 사전순으로 가장 앞에 있는 단어만 저장
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
while True:
    n = int(I())
    if n == 0:
        break
    w = I().rstrip('\n') #사전상 가장 앞서는 단어 저장
    for _ in range(n-1):
        curr = I().rstrip('\n')
        if w.lower() > curr.lower():
            w = curr
    print(w)
```