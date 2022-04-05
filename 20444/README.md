# 백준 20444번 색종이와 가위
https://www.acmicpc.net/problem/20444
---

### 문제 해결 날짜
- 2022.04.01

## 풀이 1 - 이분탐색
---
### 코드 설명
- mid는 가로 또는 세로로 자른 횟수이다.(가로 세로 구분이 없으므로)
- pieces(mid)는 색종이 조각의 수를 구하여 반환하는 함수이다.
    * n번 잘라야 하므로 세로를 mid번 자른다고 하면 가로는 n-mid번 자르게 되고, 색종이 조각의 수는 ```(mid+1)*(n-mid+1)```개가 된다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 68ms
```Python
import sys
def pieces(mid):
    return (mid+1)*(n-mid+1)
n, k = map(int, sys.stdin.readline().split())
lo, hi = -1, n
while lo+1<hi:
    mid = (lo+hi)//2
    if pieces(mid) == k:
        print('YES'); sys.exit()
    elif pieces(mid) > k: hi = mid
    else: lo = mid
print('NO')
```
---

## 풀이 2 - 이차방정식
---
### 코드 설명
- a, b를 각각 잘린 색종이의 가로개수, 새로개수라 한다. 그러면 다음과 같다.
    * ```a+b = n+2```
    * ```a*b = k```
- 위의 식으로 부터 a에 대한 이차방정식 a^2-(n+2)a+k=0을 얻을 수 있고 근의 공식에 의해서  a = (n+2+=sqrt((n+2)^2-4k))/2이다.
- 위 식의 sqrt부분을 eq라 하면 eq가 음수이면 허근이고, 정수가 아니면 a가 정수가 될 수 없어 k가 정수가 될 수 없으므로 'NO'리턴
- a = (n+2+=sqrt(eq))/2이므로 ab = ((n+2)^2-eq)/4이다. 따라서 ab=k인 것을 이용해 a,b가 음수가 아니며, 정수인 것을 체크한다.(k는 자연수이므로)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
def solve():
    eq = (n+2)**2-4*k
    if eq < 0 or int(eq**0.5)**2 != eq:
        return 'NO'
    if ((n+2)**2-eq)//4 == k:
        return 'YES'
n, k = map(int, sys.stdin.readline().split())
print(solve())
```