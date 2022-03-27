# 백준 2022번 사다리
https://www.acmicpc.net/problem/2022
---

### 문제 해결 날짜
- 2021.03.27
---

### 코드 설명
- c가 양의 실수이므로 두 빌딩 사이의 거리 w는 min(x,y)미만이다. 따라서 탐색 범위는 0,min(x,y)이다.
- c를 w를 이용하여 구하는 과정
    * c를 기준으로 왼쪽 거리를 a, 오른쪽 거리를 b라 하면 w=a+b
    * 왼쪽 빌딩의 높이를 X, 오른쪽 빌딩의 높이를 Y라 하면 b:w=c:X, a:w=c:Y 이므로 a = wc/Y, b = wc/X
    * w=a+b 이므로 w = wc/X + wc/Y, 1 = c/X + c/Y, c = XY/(X+Y)
- check(w)는 ```c <= X*Y/(X+Y)```인지 아닌지를 구하여 반환하는 함수이다.
- 오차는 10^-3까지 허용되므로 lo+10^-3 < hi 인 동안 이분탐색으로 두 빌딩 사이의 거리를 구한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
def check(w):
    X, Y = pow(x**2-w**2,0.5), pow(y**2-w**2,0.5)
    if c <= X*Y/(X+Y):
        return True
    return False
x, y, c = map(float,sys.stdin.readline().split(" "))
lo, hi = 0, min(x,y)
while lo+0.001<hi:
    mid = (lo+hi)/2
    if check(mid): lo = mid
    else: hi = mid
print("%.3f"%hi)
```