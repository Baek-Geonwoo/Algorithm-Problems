# 백준 2740번 문제
https://www.acmicpc.net/problem/2740
---

### 문제 해결 날짜 및 시간, 문제정보
- 브론즈I
- 2021.01.05
---

### 접근 방식
- 리스트 A와 B에 두 행렬을 각각 입력받아 저장
- A는 nxm, B는 mxk 행렬이므로 AB = C인 행렬 C는 nxk 행렬
- 따라서 C[i][j]를 채우려면 A의 요소와 B의 요소를 곱한 것의 m번의 합이 필요
- C의 각 항을 0으로 초기화 한 후 각 항들을 행렬곱셈을 통해 채워넣은 후 출력
---

### 소스코드
- 메모리 : 29708KB
- 시간 : 276ms
```Python
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
A = []
for i in range(n):
    A.append([int(e) for e in input().split()])
m, k = map(int,input().split())
B = []
for i in range(m):
    B.append([int(e) for e in input().split()])
C = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for h in range(m):
            C[i][j] += A[i][h]*B[h][j]
        print(C[i][j], end=" ")
    print()
```