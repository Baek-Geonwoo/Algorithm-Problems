# 백준 9024번 두 수의 합
https://www.acmicpc.net/problem/9024
---

### 문제 해결 날짜
- 2022.04.19
---

### 코드 설명
- S는 ```A[i]+A[m]```일때 diff는 현재 abs(S-K)의 최솟값이다.
- diff는 최대 200000000이므로 디폴트값을 2억으로 설정한다.
- i가 0부터 n-1까지 순회하면서 이분탐색 범위를 ```i+1~n-1까지로 하여 다음과 같이 이분탐색을 진행한다.(이분탐색 범위가 i+1~n-1인 이유는 정수쌍의 중복이 없게 하기 위해서)```
    + low, high update
        * S == K면 다음을 실행한 후 while루프 종료(A는 모두 서로 다른 정수로만 이루어져 있기 때문에 diff가 0인 또 다른 조합이 있을 수 없기 때문이다. 이 과정은 없어도 되지만 실행시간을 줄이기 위해서 추가했다.)
            + diff가 0이면 ans += 1
            + diff가 0이 아니면 diff를 0으로 초기화하고 ans=1
        * S > K 이면 high = m-1
        * S < K 이면 low = m+1
    + ans update
        * diff == abs(S-K)이면 ans += 1
        * 아니면 ans = 1, diff = abs(S-K) (diff가 더 작은 새로운 조합을 찻은 것이므로)
---

### 소스코드
- 메모리 : 264596KB
- 시간 : 1260ms
```Python
import sys
I = sys.stdin.readline
t = int(I())
for _ in range(t):
    n, K = map(int, I().split())
    A = [int(e) for e in I().split()]
    A.sort()
    diff = 200000000
    ans = 0
    for i in range(n):
        low, high = i+1, n-1
        while low <= high:
            m = (low + high)//2
            S = A[i]+A[m] 
            if S == K:
                if diff == 0:
                    ans += 1
                else:
                    diff = 0
                    ans = 1
                break
            elif S > K:
                high = m-1
            else:
                low = m+1
            if diff == abs(S-K):
                ans += 1
            elif diff > abs(S-K):
                ans = 1
                diff = abs(S-K)
    print(ans)
```
---

### 오답 노트
- 틀렸습니다.
- S == K일때 diff를 0으로 초기화 해야 하는데 이 부분을 깜빡했다.

### 오답 코드
```Python
import sys
I = sys.stdin.readline
t = int(I())
for _ in range(t):
    n, K = map(int, I().split())
    A = [int(e) for e in I().split()]
    A.sort()
    diff = 200000000
    ans = 0
    for i in range(n):
        low, high = i+1, n-1
        while low <= high:
            m = (low + high)//2
            S = A[i]+A[m] 
            if S == K:
                if diff == 0:
                    ans += 1
                else:
                    ans = 1
                break
            elif S > K:
                high = m-1
            else:
                low = m+1
            if diff == abs(S-K):
                ans += 1
            elif diff > abs(S-K):
                ans = 1
                diff = abs(S-K)
    print(ans)
```