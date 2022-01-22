# 백준 11444번 문제
https://www.acmicpc.net/problem/11444
---

### 문제 해결 날짜 및 시간, 문제정보
- 골드II
- 2021.01.07
---

### 접근 방식
- mul(A,B)는 2x2행렬을 이차원리스트로 저장한 A,B를 받아 행렬곱셈하여 각 항을 1000000007으로 나눈 나머지로 하여 반환하는 함수
- matrix_pow(M,b)는 행렬M을 b제곱하여 반환하는 함수
- fn을 n번째 피보나치 수라고 할 때 [[f1],[f0]][[1,1],[1,0]]^(n-1)=[[fn],[fn-1]]
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 92ms
```Python
import sys
input = sys.stdin.readline
def mul(A,B):
    C = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
    for i in range(2):
        for j in range(2):
            C[i][j] %= 1000000007
    return C
def matrix_pow(M,b):
    if b == 1:
        return M
    elif b == 2:
        return mul(M,M)
    else:
        N = matrix_pow(M,b//2)
        if b%2:
            return mul(mul(N,N),M)
        return mul(N,N)
n = int(input())
F = [[1],[0]] #F1과 F0
A = [[1,1],[1,0]] #Fn을 구할 때 필요한 2x2행렬
if n > 1:
    M = matrix_pow(A,n-1)
    B = [[0],[0]]
    for i in range(2):
        for j in range(2):
            B[i][0] += M[i][j]*F[j][0]
        B[i][0] %= 1000000007
    print(B[0][0])
else:
    print(F[-n-1])
```