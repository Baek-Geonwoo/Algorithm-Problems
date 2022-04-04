# 백준 17179번 케이크 자르기
https://www.acmicpc.net/problem/17179
---

### 문제 해결 날짜
- 2022.04.04
---

### 코드 설명
- check(m)은 가장 작은 조각의 길이가 m 이상으로 잘랐을 때 Q번 이상 자를 수 있는지를 구하여 반환하는 함수이다.
    * cut > Q 일때가 Q번 이상 자를 수 있을 때인 이유는 S에 L을 더해서 마지막으로 자른 위치 ~ 케이크 오른쪽 끝까지의 거리가 m 이상이어야 마지막으로 자른 위치가 유효하기 때문이다. 즉 가장 오른쪽 조각의 길이도 m 이상이어야 하기 때문이다.ㄴ
- 범위는 while문 조건식이 lo+1 < hi이므로 해답 범위 (1,L)에서 0 ~ L이다. 따라서 lo=0, hi=L로 초기화, 이 범위는 가장 작은 조각의 길이의 범위이다.
- 가장 작은 조각의 길이의 최댓값을 구하는 것이고, while문이 끝나기 전에 마지막으로 check(mid)가 참일 때의 lo가 Q번 자르는 것을 만족하므로(답이 될 수 있으므로) lo를 출력
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 1316ms
```Python
import sys
def check(m):
    cut = 0
    left = 0
    for right in S:
        if right-left>=m:
            left = right
            cut += 1
    if cut > Q: return True
    return False
I = sys.stdin.readline
N, M, L = map(int, I().split())
S = [int(I()) for _ in range(M)]+[L]
for _ in range(N):
    Q = int(I())
    lo, hi = 0, L
    while lo+1<hi:
        mid = (lo+hi)//2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)
```