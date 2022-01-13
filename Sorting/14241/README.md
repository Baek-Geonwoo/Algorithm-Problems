# 백준 14231번 문제
https://www.acmicpc.net/problem/14231
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버II
- 2021.01.13
---

### 접근 방식
- S는 크기가 n인 리스트로 슬라임 크기들을 저장 / score에는 점수 저장
- temp에는 ~S[i]까지의(0 <= i < n) S의 요소들의 합이 저장
- S를 오름차순 정렬(크기가 작은 슬라임들부터 합쳐야 점수가 최대가됨 -> 작은 수들을 합쳐 큰수를 만들면 큰 수들끼리의 곱이 되고 점수가 최대가 됨)
- i번째 슬라임을 합칠 때 얻을 수 있는 점수는 (S[0]+...+S[i-1])xS[i]
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
n = int(I())
S = [int(e) for e in I().split()]
S.sort()
temp = S[0]
score = 0
for i in range(1,n):
    score += temp*S[i]
    temp += S[i]
print(score)
```