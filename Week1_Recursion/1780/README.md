# 백준 1780번 문제
https://www.acmicpc.net/problem/1780
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버II
- 2021.12.30
---

### 접근 방식
- nxn종이 정보를 입력받아 저장할 2차원 리스트 P에 저장 D는 3가지 수가 적힌 종이의 개수를 저장할 딕셔너리
- solve(x,y,n)은 n이 1이라면 D[P[x][y]]에 1을 추가
- n이 1이 아니라면 P[x][y]를 기준으로 오른쪽 아래방향으로 nxn범위가 모두 같은 수가 적힌 것인지 확인하고 그렇다면, D[P[x][y]]에 1을 추가, 그렇지 않다면 n//3xn//3으로 nxn범위를 9개로 분할하여 solve를 재귀호출
---

### 소스코드
- 메모리 : 371328KB
- 시간 : 4040ms
```Python
import sys
input = sys.stdin.readline
def solve(x,y,n):
    if n == 1:
        D[P[x][y]] += 1
        return
    is_same = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if P[x][y] != P[i][j]:
                is_same = False
                break
    if is_same:
        D[P[x][y]] += 1
    else:
        for i in range(3):
            for j in range(3):
                solve(x+i*(n//3),y+j*(n//3),n//3)
n = int(input())
P = [input().rstrip('\n').split() for _ in range(n)]
D = {'-1':0,'0':0,'1':0}
solve(0,0,n)
for i in range(-1,2):
    print(D[str(i)])
```