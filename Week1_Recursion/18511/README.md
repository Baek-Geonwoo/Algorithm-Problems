# 백준 18511번 문제
https://www.acmicpc.net/problem/18511
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2021.12.27
---

### 접근 방식
- 높은 자리수부터, 큰 숫자부터 구성
- pos(10의 지수 3자리수면 2)가 -1이 되면 재귀종료, 단, 수는 0이 아닌 숫자들로만 구성되어야 하므로 0이 포함된 경우는 제외
- 재귀가 끝나면 답을 저장하는 변수에 재귀가 끝났을 때 구해진 수중 큰 수를 변수에 저장
---

### 소스코드
- 메모리 : 29200KB
- 시간 : 68ms
```Python
def sol(pos,num):
    global ans
    if pos == -1:
        if '0' not in str(num):
            ans = max(ans, num)
        return
    for i in range(k):
        curr = A[i]*10**pos+num
        if curr <= n:
            sol(pos-1, curr)
        else:
            sol(pos-1, num)

n, k = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
sol(len(str(n))-1,0)
print(ans)
```