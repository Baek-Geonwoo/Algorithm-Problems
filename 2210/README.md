# 백준 2210번 숫자판 점프
https://www.acmicpc.net/problem/2210
---

### 문제 해결 날짜
- 2021.02.10
---

### 코드 설명
- is_in은 x, y가 A의 음이 아닌 인덱스에 해당하는지 체크하는 함수, dx, dy는 순서대로 상하좌우로 이동할 때의 인덱스 변화를 저장한 리스트
- 시작지점 25군데에서 각각 solution을 호출한다.
- solution함수에서 ans의 크기가 6이면 재귀를 종료하는데 S = "".join(ans)라 하고 Set.add(S) 하여 S의 중복이 없게 Set에 답들을 저장한다.
- ans 크기가 6이 아니라면 x,y를 기준으로 상하좌우의 인덱스(X,Y)가 5x5범위 안에 있는지 is_in으로 체크한 후 존재하면 ans에 ```A[X][Y]를 넣고 그 위치에서 solution을 재귀호출한 후 ans에서 그 요소를 다시 pop한다.```
---

### 소스코드
- 메모리 : 31372KB
- 시간 : 84ms
```Python
import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]
D = {}
def is_in(x,y):
    if 0<=x<5 and 0<=y<5:
        return True
    return False

def solution(x,y):
    if len(ans) == 6:
        S = "".join(ans)
        try:
            if D[S]:
                pass
        except:
            D[S] = True
        return
    for i in range(4):
        X, Y = x+dx[i], y+dy[i]
        if is_in(X, Y):
            ans.append(A[X][Y])
            solution(X, Y)
            ans.pop()

I = sys.stdin.readline
A = [I().split() for _ in range(5)]
for x in range(5):
    for y in range(5):
        ans = [A[x][y]]
        solution(x, y)
print(len(D))
```