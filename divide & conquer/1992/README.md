# 백준 1992번 문제
https://www.acmicpc.net/problem/1992
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버I
- 2021.01.03
---

### 접근 방식
- solve함수는 시작 위치 x,y(Q[x][y])와 Q의 크기 n을 매개변수로 받는다.
- x,y에서 시작해서 nxn범위의 값이 모두 같은지 확인하여 모두 같으면 Q[x][y]를 반환하고 같지 않으면 n//2xn//2범위로 4분할해서 solve함수를 재귀적으로 4번 호출
- 결과는 ()로 감싸서 반환
---

### 풀이1 소스코드
- 메모리 : 29200KB
- 시간 : 68ms
```Python
import sys
input = sys.stdin.readline
def solve(x,y,n):
    if n == 1:
        return Q[x][y]
    isSame = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if Q[x][y] != Q[i][j]:
                isSame = False
                break
    if isSame:
        return Q[x][y]
    return '('+solve(x,y,n//2)+solve(x,y+n//2,n//2)+solve(x+n//2,y,n//2)+solve(x+n//2,y+n//2,n//2)+')'
n = int(input())
Q = [list(input().rstrip('\n')) for _ in range(n)]
print(solve(0,0,n))
```