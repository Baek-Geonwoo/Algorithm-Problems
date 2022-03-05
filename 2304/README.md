# 백준 2304번 창고 다각형
https://www.acmicpc.net/problem/2304
---

### 문제 해결 날짜
- 2021.03.04
---

### 코드 설명
- h_index, h는 각각 H가 최대인 기둥들의 인덱스들의 리스트, h는 그 높이이다. P의 요소들(L,H)을 입력받으면서 h_index, h에 알맞은 값을 저장한다.
- H가 h인 기둥들은 그 사이의 높이가 항상 h이므로 높이가 h이면서 index가 최소인 기둥(a)과 최대인 기둥(b) 사이의 거리+1(+1을 하는 이유는 L은 왼쪽 위치이므로 오른쪽 기둥을 포함시키기 위해서)에 h를 곱한 값을 ans의 초기값으로 한다.
- 인덱스 1부터 a까지, 인덱스 N-1부터 b까지 순회하며 현재까지 가장 높은 기둥(prev)보다 높이가 높은 기둥이 나오면 높이를 prev로 하여 둘 사이의 넓이를 구해 ans에 추가한다. 즉, 인덱스 0부터 가장 높은 기둥까지, 인덱스 N-1부터 가장 높은 기둥까지 넓이를 구해 ans에 더한다.
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 68ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
P = [tuple(map(int, I().split())) for _ in range(N)]
h_index, h = [], 0
P.sort()
for i in range(N):
    if h < P[i][1]:
        h_index = []
        h_index.append(i)
        h = P[i][1]
    elif h == P[i][1]:
        h_index.append(i)
ans = h*(P[h_index[-1]][0]-P[h_index[0]][0]+1)
prev_L, prev = P[0][0], P[0][1]
for i in range(1,h_index[0]+1):
    if prev < P[i][1]:
        ans += prev*(P[i][0]-prev_L)
        prev_L, prev = P[i][0], P[i][1]
prev_L, prev = P[N-1][0], P[N-1][1]
for i in range(N-2,h_index[-1]-1,-1):
    if prev < P[i][1]:
        ans += prev*(prev_L-P[i][0])
        prev_L, prev = P[i][0], P[i][1]
print(ans)
```