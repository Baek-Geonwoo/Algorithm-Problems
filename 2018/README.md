# 백준 2018번 수들의 합 5
https://www.acmicpc.net/problem/2018
---

### 문제 해결 날짜
- 2021.01.29
---

### 접근 방식
- s, e는 각각 1 ... N의 수들이 있는 리스트에서 구간에서 가장 작은 수와 가장 큰 수이며, S에 s부터e까지의 합이 cnt에 합이 N인 구간의 개수를 저장한다.
- s <= e이며 s <= N인 동안 while 루프 안에서 S에 따라 세가지 경우로 나누어 s, e를 조작한다.
    + S < N인 경우
        * e가 N 이하이면 S에 e를 더하고 e를 1 증가시킨다.
        * e가 N보다 크다면 S가 더이상 증가할 수 없으므로 루프를 종료한다.
    + S > N인 경우 S에서 s를 뺴고 s를 1 증가시킨다.
    + S == N인 경우 cnt를 1 증가시킨다.
        * e가 N 이하일 경우 S에서 s를 빼고 s를 1 증가시킨다.
        * e가 N보다 크다면 s를 증가시켜도 더이상 S가 N이 될 수 없으므로 루프를 종료한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 4504ms
```Python
import sys
N = int(sys.stdin.readline())
s, e = 1, 1
S = 0
cnt = 0
while s <= e and s <= N:
    if S < N:
        if e <= N:
            S += e
            e += 1
        else:
            break
    elif S > N:
        S -= s
        s += 1
    else:
        cnt += 1
        if e > N:
            break
        else:
            S -= s
            s += 1
print(cnt)
```