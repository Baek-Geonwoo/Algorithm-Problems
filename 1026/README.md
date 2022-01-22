# 백준 1026번 문제
https://www.acmicpc.net/problem/1026
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버IV
- 2021.01.11
---

### 접근 방식
- S = A[0]*B[0]+ ... A[n-1]*B[n-1]
- 두 수의 곱에서 S가 가장 크려면 A[i]*B[i](0<=i<n)에서 A[i]와 B[i]의 차이가 가장 작아야 함
- 따라서 A, B를 오름차순 정렬한 후 인덱스 순서대로 곱한 것이 가장 작은 S
- 문제에서는 B는 재배열하면 안된다고 적혀 있었지만, A, B를 오름차순 정렬해서 가장 작은 S를 구한 후 그 쌍에 맞게 A를 B에 대응시켜 재배열
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
n = int(I())
A = [int(e) for e in I().split()]
B = [int(e) for e in I().split()]
A.sort()
B.sort(reverse=True)
S = 0
for i in range(n):
    S += A[i]*B[i]
print(S)
```