# 백준 14719번 빗물
https://www.acmicpc.net/problem/14719
---

### 문제 해결 날짜
- 2021.03.25
---

### 코드 설명
- A는 W크기의 리스트이고 ```A[i]에는 i번 위치에 고이는 빗물의 양이 저장된다.```
- 양 끝은 빗물이 고일 수 없으므로 range(1,W-1)을 왼쪽과 오른쪽 방향으로 탐색하여 각각 high(현재까지 가장 높은 블록의 높이)를 ```B[0], B[-1]```로 하여 현재 위치의 블록이 high보다 작으면 그 차이를 ```A[i]에 저장하고, 오른쪽방향으로 탐색할 때는 현재 A[i]에 저장된 값과, 현재 구한 값 중 작은 값을 A에 저장한다.```
- A가 모두 채워지면 sum(A)이 고일 수 있는 빗물의 총량이다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
H, W, *B = map(int, sys.stdin.read().split())
A = [0]*W
high = B[0]
for i in range(1,W-1):
    A[i] = max(0,high-B[i])
    high = max(high,B[i])
high = B[-1]
for i in range(W-2,0,-1):
    A[i] = min(A[i],max(0,high-B[i]))
    high = max(high,B[i])
print(sum(A))
```