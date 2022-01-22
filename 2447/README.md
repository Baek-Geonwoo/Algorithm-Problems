# 백준 2447번 문제
https://www.acmicpc.net/problem/2447
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버I
- 2021.12.31
---

### 풀이1 접근 방식
- star함수는 S[x][y]를 시작으로 오른쪽 아래로 n//3xn//3범위에 문제 규칙대로 별이 찍힐 위치의 S[x][y]는 1로 변경
- star함수를 실행한 후 S 리스트를 출력
---

### 풀이1 소스코드
- 메모리 : 66132KB
- 시간 : 3516ms
```Python
def star(x,y,n):
    if n == 1:
        S[x][y] = 1
        return
    for i in range(x,x+n,n//3):
        for j in range(y,y+n,n//3):
            if i==x+n//3 and j==y+n//3:
                continue
            star(i,j,n//3)
n = int(input())
S = [[0]*n for i in range(n)]
star(0,0,n)
for i in range(n):
    for j in range(n):
        if S[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()
```
---
### 풀이2 접근 방식
- n이 3이면 '***' '* *' '***'을 담은 리스트를 반환
- ret 리스트에 이전 재귀함수로부터 받은 리스트를 문제 규칙에 맞게 변형하여 append 한 뒤 리턴
- ret 리스트에는 최종적으로 n줄의 별 패턴이 저장
---

### 풀이2 소스코드
- 메모리 : 38548KB
- 시간 : 76ms
```Python
import sys
def star(n):
    if n == 3:
        return ['***','* *','***']
    ret = []
    S = star(n//3)
    for s in S:
        ret.append(s*3)
    for s in S:
        ret.append(s+' '*(n//3)+s)
    for s in S:
        ret.append(s*3)
    return ret
n = int(input())
print('\n'.join(star(n)))
```