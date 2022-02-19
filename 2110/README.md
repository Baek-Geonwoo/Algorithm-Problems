# 백준 2110번 공유기 설치
https://www.acmicpc.net/problem/2110
---

### 문제 해결 날짜
- 2021.02.20
---

### 코드 설명
- m은 두 공유기 사이의 최소거리이다. 맨 앞에서부터 간격 m 이상으로 공유기를 설치한다.
    * 설치된 공유기가 C개 이상이면 간격을 더 늘릴 수 있다는 것이므로 ans를 m으로 update하고, low=m+1한다.
    * 설치된 공유기가 C개 미만이면 간격을 줄여야 한다는 것이므로 high=m-1한다.
---

### 소스코드
- 메모리 : 38588KB
- 시간 : 700ms
```Python
import sys
I = sys.stdin.readline
N, C = map(int, I().split())
H = [int(I()) for _ in range(N)]
H.sort()
low, high = 1, H[-1] - H[0]
ans = 0
while low <= high:
    m = (low+high)//2
    curr = H[0]
    cnt = 1
    for i in range(1,N):
        if H[i] >= curr + m:
            cnt += 1
            curr = H[i]
    if cnt >= C:
        ans = m
        low = m+1
    else:
        high = m-1
print(ans)
```