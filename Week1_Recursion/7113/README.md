# 백준 7113번 문제
https://www.acmicpc.net/problem/7113
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2021.12.27
---

### 접근 방식
- 현재 상황의 n,m에서 둘 중 큰 값을 n, 작은 값을 m이라 함
- cnt(현재 정사각형 개수)에 현재 자를 수 있는 가장 큰 정사각형이 m*m인 정사각형이므로 cnt += n//m
- n에서 n//m*m을 빼주고 다음 재귀로 넘어감, n과 m중 하나라도 0이면 종료된 것이므로 cnt 출력하고 재귀 종료
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 64ms
```Python
def sol(n, m, cnt):
    if n*m == 0:
        print(cnt)
        return
    n, m = max(n,m), min(n,m)
    cnt += n//m
    n -= n//m*m
    sol(n,m,cnt)

n,m = map(int,input().split())
sol(n,m,0)
```