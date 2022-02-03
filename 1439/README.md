# 백준 1439번 뒤집기
https://www.acmicpc.net/problem/1439
---

### 문제 해결 날짜
- 2021.02.03
---

### 접근 방식
- 그리디 기준 : 연속된 0, 1을 각각 0, 1 묶음이라 할 때 묶음 수가 적은 숫자를 뒤집는다.
- ```prev=S[0], num[S[0]]+=1 한 후 S의 인덱스 i가 1~끝까지 순회하면서 prev!=S[i]일 때 S[i] 묶음이 1 추가되는 식으로 0, 1 묶음의 수를 구한다.```
- 11111, 0000 같이 뒤집을 필요가 없는 문자열은 0, 1 묶음 수의 합이 1이므로 이때는 0을 출력한다.
- 위 경우가 아니면 둘 중 적은 묶음의 숫자를 뒤집는다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
S = sys.stdin.readline().rstrip('\n')
num = {'0':0, '1':0}
prev = S[0]
num[S[0]] += 1
for i in range(1,len(S)):
    if S[i] != prev:
        num[S[i]] += 1
        prev = S[i]
if num['0'] + num['1'] == 1:
    print(0)
else:
    print(min(num['0'], num['1']))
```