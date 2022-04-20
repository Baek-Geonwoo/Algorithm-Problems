# 백준 9082번 지뢰찾기
https://www.acmicpc.net/problem/9082
---

### 문제 해결 날짜
- 2022.04.20
---

### 코드 설명
- `* 즉, 지뢰가 묻힌 것이 확실한 곳과 그 주변의 지뢰 개수를 1씩 줄이고 mine += 1`
- 그 다음 3, 2 순으로 순회하며 그 위치에 지뢰가 있다고 보고 주변 지뢰 개수를 1씩 줄이고 mine += 1 (3, 2 주변에는 0이 있을 수 없으므로)
- mine에 s = sum(num)을 3으로 나눈 몫을 더하고 나머지가 0이 아니면 1을 더 더한다.
---

### 소스코드
- 메모리 : 30840KB
- 시간 : 64ms
```Python
import sys
def input():
    return sys.stdin.readline().rstrip()
def in_range(x):
    if 0 <= x < N: return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int, input()))
    land = list(input())
    mine = 0
    for i in range(N):
        if land[i] == '*':
            for j in range(i-1,i+2):
                if in_range(j):
                    num[j] -= 1
            mine += 1
    for i in range(3,1,-1):
        for j in range(N):
            cnt = 0
            if num[j] == i:
                for k in range(j-1,j+2,2):
                    if in_range(k) and num[k]:
                        cnt += 1
                    else:
                        cnt = 0
                        break
                if cnt >= 2:
                    mine += 1
                    for k in range(j-1,j+2):
                        num[k] -= 1
    s = sum(num)
    mine += s//3 + (s%3!=0)
    print(mine)
```