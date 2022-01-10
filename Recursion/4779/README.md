# 백준 4779번 문제
https://www.acmicpc.net/problem/4779
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버III
- 2021.12.29
---

### 접근 방식
- 입력이 끝나면 while문이 종료되도록 예외처리사용
- solve 함수의 n은 칸토어 집합의 단계, x는 시작점 C는 칸토어 집합을 저장할 리스트
- x를 시작점으로 칸토어 집합의 n-1단계, x+3^(n-1)부터 x+2x3^(n-1)-1까지 공백(칸토어 집합의 n단계), x+2x3^(n-1)을 시작점으로 n-1단계를 실행
---

### 소스코드
- 메모리 : 34732KB
- 시간 : 148ms
```Python
import sys
input = sys.stdin.readline
def solve(n,x):
    if n == 0:
        return
    solve(n-1,x)
    for i in range(x+3**(n-1),x+2*3**(n-1)):
        C[i] = " "
    solve(n-1,x+2*3**(n-1))
while True:
    try:
        n = input()
        n = int(n)
        C = ["-"]*3**n
        solve(n,0)
        print("".join(C))
    except:
        break
```