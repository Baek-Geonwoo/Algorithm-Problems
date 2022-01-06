# 백준 10830번 문제
https://www.acmicpc.net/problem/10830
---

### 문제 해결 날짜 및 시간, 문제정보
- 골드IV
- 2021.01.06
---

### 접근 방식
- mul(A,B)는 행렬을 저장한 2차원 리스트 A,B를 받아 행렬곱셈하여 반환하는 함수
- matrix_pow(M,b)는 행렬 M을 b제곱하여 반환하는 함수
- matrix_pow는 b를 2가 될 때까지(b=1일때도 대응) 2로 나누어 구한다음 제곱하여 M^b를 구함
- matrix_pow(M,b) = matrix_pow(M,b)^2 = mul(N,N) (N = matrix_pow(M,b)라고 할 때)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
input = sys.stdin.readline
def mul(A,B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    for i in range(n):
        for j in range(n):
            C[i][j] %= 1000
    return C
def matrix_pow(M,b):
    n = len(M)
    if b == 1:
        return M
    elif b == 2:
        return mul(M,M)
    else:
        N = matrix_pow(M,b//2)
        if b%2:
            return mul(mul(N,N),M)
        return mul(N,N)

n, b = map(int,input().split())
A = []
for i in range(n):
    A.append([int(e) for e in input().split()])
M = matrix_pow(A,b)
for i in range(n):
    for j in range(n):
        print(M[i][j]%1000,end=" ")
    print()
```