# 백준 2140번 지뢰찾기
https://www.acmicpc.net/problem/2140
---

### 문제 해결 날짜
- 2021.03.08
---

### 코드 설명
- 지뢰가 놓일 수 있는 곳은 테두리를 제외한 나머지 칸이므로 ans의 초기값은 max(N-2,0)^2이다.(N이 1인 경우도 있으므로)
- 숫자가 적힌 테두리 바로 안쪽을 돌면서 주변에 0이 적힌 칸이 없으면 그 칸에 지뢰가 있을 수 있으므로 ans += 1한다 그 후 해당 칸 주변 8칸의 수를 -1해준다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
M = [[int(e) if e.isdigit() else e for e in list(I().strip())] for _ in range(N)]
ans = max(N-4,0)**2
d = (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)
for x in range(1,N-1):
    for y in (1,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
for x in (1,N-2):
    for y in range(2,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
print(ans)
```
---
### 오답노트
- 아래 코드는 위의 정답코드에서 for문의 순서만 바꾼 것이다. 아래 코드처럼 하면 가장 바깥에 있는 #들의 모서리 부분부터 시작하는 것이 아니라 중간 부분부터 시작하기 때문에 121->```*#*```처럼 중간이 비어있고 그 양옆에 지뢰가 있을 수 있는 경우에 논리 오류가 발생한다.
- 해당 오류가 있는지 체크할 수 있는 테스트케이스, 인덱스 5,2 에서 해당 논리 오류가 발생한다.
```
7
1221000
2#####0
3#####1
2#####2
2#####2
1#####1
1121100
```

### 오답코드
```Python
import sys
I = sys.stdin.readline
N = int(I())
M = [[int(e) if e.isdigit() else e for e in list(I().strip())] for _ in range(N)]
ans = max(N-4,0)**2
d = (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)
for x in (1,N-2):
    for y in range(2,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
for x in range(1,N-1):
    for y in (1,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
print(ans)
```