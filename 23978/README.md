# 백준 23978번 급상승
https://www.acmicpc.net/problem/23978
---

### 문제 해결 날짜
- 2021.03.26
---

### 코드 설명
- check 함수는 가격을 X원으로 올렸을 때 K원 이상 현금화가 가능한지를 구하여 반환하는 함수이다.
- 마지막 날은 무조건 X, X-1 ... 3, 2, 1, 0원으로 X원부터 0원까지 현금화되므로 현금화 가능 금액 S의 초기값은 1부터 X까지의 합이다.
- 코인의 금액은 음수가 될 수 없으므로 x보다 ```코인 가격 하락 기간(A[i+1]-A[i])과 x중 작은 수를 d로 하면 A[i+1]-A[i]일 동안 현금화 할 수 있는 금액은 d*(x+x-d+1)//2원이다.```
- ```위 방식대로 i가 0부터 N-2까지 A[i]일 부터 A[i+1]-1일 까지의 코인 가격의 합을 S에 더하여 K원 이상 현금화가 가능한지를 구한다.``` (중간에라도 S가 K이상이면 K원 이상 현금화가 가능한 것이므로 실행시간 감소를 위해 return False)
- check함수를 이용하여 이분탐색으로 X의 최솟값을 구한다.
---

### 소스코드
- 메모리 : 274640KB
- 시간 : 456ms
```Python
import sys
def check(x):
    S = x*(x+1)//2
    for i in range(N-1):
        d = min(x, A[i+1]-A[i])
        S += d*(x+x-d+1)//2
        if S >= K:
            return True
    if S >= K:
        return True
    return False
N, K, *A = map(int, sys.stdin.read().split())
lo, hi = 0, int(1e18)
while lo+1<hi:
    mid = (lo+hi)//2
    if check(mid):
        hi = mid
    else:
        lo = mid
print(hi)
```