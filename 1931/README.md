# 백준 1931번 회의실 배정
https://www.acmicpc.net/problem/1931
---

### 문제 해결 날짜
- 2021.01.27
---

### 접근 방식
- 그리디 기준 : 가장 빨리 끝나는 회의부터 배정한다.
    * 가장 빨리 끝나는 회의(a)부터 배정하면 남은 시간이 다른 경우보다 더 많다.
    * 위 가설을 증명하기 위해 a보다 늦게 끝나는 회의(b)부터 배정하고 시작했을 때 더 많은 회의를 배정할 수 있다고 가정하면, 남은 시간이 당연히 a보다 더 적고, 회의 목록은 같으므로 남은 시간이 더 적은 b부터 배정한 경우가 당연히 배정할 수 있는 회의 수가 더 적다. 앞의 가설의 대우를 부정했을 때 모순이 발생하므로 대우는 참이고, 따라서 앞서 세운 가설은 참이다.
- 회의의 시작과 끝 ```[s,e]```들을 입력받아 A에 저장한 후 e, s 순으로 우선순위로 A를 오름차순 정렬한 후 앞서 증명한 그리디 기준대로 가장 빨리 끝나는 회의부터 배정하고, 그 회의와 시간이 겹치지 않도록 같은 기준으로 계속 회의를 배정하여 그 수를 cnt에 저장한다.
---

### 소스코드
- 메모리 : 59828KB
- 시간 : 356ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
A = [list(map(int,I().split())) for _ in range(N)]
A.sort(key = lambda x: [x[1], x[0]])
curr_time = 0
cnt = 0
for s,e in A:
    if curr_time <= s:
        curr_time = e
        cnt += 1
print(cnt)
```
---
### 오답노트
- 처음에 아래 코드와 같이 A를 정렬할 때 ```x[1]```, 즉, e만을 기준으로 A를 오름차순 정렬하여 회의시작시간은 정렬에 고려되지 않아 ```[10, 11], [9,11]``` 같은 경우 당연히 ```[9,11], [10,11]``` 순으로 정렬되어야 함에도 그렇게 되지 않아 오답이 나왔었다. 그래서 위 코드처럼 s도 e다음으로 고려하여 정렬되도록 수정하여 통과했다.

### 오답코드
```Python
import sys
I = sys.stdin.readline
N = int(I())
A = [list(map(int,I().split())) for _ in range(N)]
A.sort(key = lambda x: x[1])
curr_time = 0
cnt = 0
for s,e in A:
    if curr_time <= s:
        curr_time = e
        cnt += 1
print(cnt)
```