# 백준 16592번 문제
https://www.acmicpc.net/problem/16592
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버IV
- 2021.12.29
---

### 접근 방식
- 1부터 A까지, 1부터 B까지 끝이 0으로 끝나는 수들 중 문제의 기준 상 홀수인 수들의 개수를 o라 하고 구하는 함수 solve
- 1부터 n까지 홀수의 개수(odd)는 ceil(n/2), 짝수(even)의 개수는 n//2이므로 문제의 기준 상 1부터 n까지 홀수는 odd + o, 짝수는 even - o
- pos는 오른쪽 끝부터 자리수(10의 자리수면 pos는 2)
- A와 B를 포함해서 A부터 B까지 홀짝을 구분하는 것이므로 1부터 B까지 구한 결과에서 1부터 A까지 구한 결과를 빼서 구하고, 여기서 A는 제외되므로 A가 홀인지 짝인지를 구하여 답에 반영하여 출력함
---

### 소스코드
- 메모리 : 31312KB
- 시간 : 68ms
```Python
from math import ceil
def solve(n,pos): # 1부터 n까지 0으로 끝나는 수 중 문제 조건 상 홀수 개수 구하는 함수
    # pos는 가장 큰 자리수의 0의 위치 1이면 1의자리수 2면 10의자리수
    if pos == len(n):
        return
    global odd
    odd += ceil(int(n[:-pos])/2)
    solve(n,pos+1)

A, B = map(int,input().split())
odd = 0 # 0으로 끝나는홀수번호판의 개수
solve(str(A),1)
oddA = ceil(A/2) + odd
evenA = A//2 - odd
odd = 0
solve(str(B),1)
oddB = ceil(B/2) + odd
evenB = B//2 - odd
odd = oddB-oddA
even = evenB-evenA
#A를 포함한 범위이므로 A를 포함시키기 위해서
if int(str(A).replace("0","")[-1])%2:
    odd += 1
else:
    even += 1
print(odd, even)
```