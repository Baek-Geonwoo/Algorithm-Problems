# 백준 1072번 게임
https://www.acmicpc.net/problem/1072
---

### 문제 해결 날짜
- 2022.03.24
---

### 코드 설명
- check 함수는 M번 김형택이 게임을 M번 더 이겼을 때 승률이 변하는지를 구하여 반환하는 함수이다.
- 승률이 에초에 99%이상이면 아무리 게임을 더 해도 승률이 변하지 않으므로 -1을 출력한다.
- 이분탐색 범위는 최소 1번은 더 이겨라 변화가 있을 수 있고, X의 최댓값이 10^9이므로 0, 1,000,000,000로 한다.
- 이분탐색을 통해서 김형택이 승률을 변하게 하기 위한 최소 승리 횟수를 구한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
def check(M):
    if (Y+M)*100//(X+M) != Z:
        return True
    return False
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X
if Z >= 99:
    print(-1)
else:
    low, high = 0, 10**9
    while low+1 < high:
        mid = (low + high)//2
        if check(mid): high = mid
        else: low = mid
    print(high)
```