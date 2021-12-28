# 백준 16505번 문제
https://www.acmicpc.net/problem/16505
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버IV
- 2021.12.29
---

### 접근 방식
- **이 3^(n-1)개 반복되는 프렉탈 구조
  *
- 각 인덱스가 0으로 초기화 된 2^n x 2^n 인 2차원 리스트 S에 특정 칸이 *면 1로 변경
- x,y칸에서 solve 함수가 실행되면, 현재 칸과 x+2^(n-1),y칸, x,y+2^(n-1)칸에서 n이 n-1로 solve를 재귀호출
- solve 함수를 실행하여 S가 모두 적절하게 채워지면 S[x][y]가 1인지 0인지에 따라 각 칸에 맞게 빈칸과 "*"를 출력
---

### 소스코드
- 메모리 : 36912KB
- 시간 : 376ms
```Python
def solve(n,x,y):
    if n == 0:
        S[x][y] = 1
        return
    solve(n-1,x,y)
    solve(n-1,x+2**(n-1),y)
    solve(n-1,x,y+2**(n-1))

n = int(input())
S = [[0]*2**n for i in range(2**n)]
solve(n,0,0)
for i in range(2**n):
    for j in range(2**n-i):
        if S[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()
```