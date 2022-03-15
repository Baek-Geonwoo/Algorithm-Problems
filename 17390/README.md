# 백준 17390번 이건 꼭 풀어야 해!
https://www.acmicpc.net/problem/17390
---

### 문제 해결 날짜
- 2021.03.15
---

### 코드 설명
- A를 입력받아 비내림차순 정렬한다.(비내림차순은 중복된 항이 있을 수 있는 오름차순이다.)
- ```P[i]에 A[0] + ... +A[i-1]까지의 합을 저장한다. P=A[:]한 후 i가 1부터 N-1까지 P[i] += P[i-1]을 하면되기 때문에 O(N)시간이 걸린다.```
- ```문제에서 L, R을 인덱스가 아니라 순서로 주기 때문에 P.insert(0.0)으로 P의 맨 앞에 0을 추가한다.```
- L, R을 Q번 입력받아 ```각각의 L, R에 대해서 P[R]-P[L-1]을 출력한다.(P[L-1]을 빼는 이유는 그렇게 해야 P[R]-P[L-1]이 A의 L번째 항+ ... +A의 R번째 항이 되기 때문이다. 즉, A의 L번째 항을 포함시켜야 하기 때문)```
---

### 소스코드
- 메모리 : 62708KB
- 시간 : 928ms
```Python
import sys
I = sys.stdin.readline
N, Q = map(int, I().split())
A = [int(e) for e in I().split()]
A.sort()
P = A[:]
for i in range(1,N):
    P[i] += P[i-1]
P.insert(0,0)
for _ in range(Q):
    L, R = map(int, I().split())
    print(P[R]-P[L-1])
```