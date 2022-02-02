# 백준 2217번 로프
https://www.acmicpc.net/problem/2217
---

### 문제 해결 날짜
- 2021.02.02
---

### 접근 방식
- 그리디 기준: 최대중량이 적은 로프부터 그 로프의 최대중량을 w/k로 한다.
- 로프들의 최대중량(리스트 R)을 오름차순으로 정렬한다.
- 최대중량이 적은 로프부터 그 로프의 최대중량을 w/k로 하여 w를 구하는데 이렇게 구할 수 있는 w중 최댓값을 구한다.
    * ```예를 들어 R[i]면 w/k = R[i]이므로 w = R[i] * (N-i)이다.```
---

### 소스코드
- 메모리 : 34080KB
- 시간 : 144ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
R = [int(I()) for _ in range(N)]
R.sort()
# 그리디 기준: 최대중량이 적은 로프부터 그 로프가 최대한 견딜 수 있게 w/k설정
W = 0
for i in range(N):
    W = max(W, R[i]*(N-i))
print(W)
```