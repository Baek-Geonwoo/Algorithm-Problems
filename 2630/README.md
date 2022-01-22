# 백준 2630번 문제
https://www.acmicpc.net/problem/2630
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버III
- 2021.12.29
---

### 접근 방식
- solve함수의 e는 탐색 단위, e가 4면 4x4영역이 모두 같은 색인지 탐색
- solve함수의 x,y는 탐색 시작위치 e x e범위의 색이 시작 위치와 모두 같은지 체크, 만약 다른 색이 나오면 x,y를 기준으로 e//2 x e//2크기의 4개 영역으로 나누어 solve를 재귀호출, 모두 같다면 p(0번 인덱스는 흰색, 1번 인덱스는 파란색 종이 수 저장)에 색에 따라서 색종이 수 +1
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 80ms
```Python
import sys
input = sys.stdin.readline
n = int(input())
paper = [[int(e) for e in input().split()] for i in range(n)]
p = [0,0] #순서대로 하얀색 파란색
def solve(x,y,e):
    color = paper[x][y]
    for i in range(x,x+e):
        for j in range(y,y+e):
            if color != paper[i][j]:
                solve(x,y,e//2)
                solve(x+e//2,y,e//2)
                solve(x,y+e//2,e//2)
                solve(x+e//2,y+e//2,e//2)
                return
    p[color] += 1
    return
solve(0,0,n)
for i in range(2):
    print(p[i])
```