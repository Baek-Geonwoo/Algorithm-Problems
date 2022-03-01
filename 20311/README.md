# 백준 20311번 화학 실험
https://www.acmicpc.net/problem/20311
---

### 문제 해결 날짜
- 2021.03.04
---

### 코드 설명
- ci들을 입력받아 (-ci, i)쌍으로 최대 힙 H 선언한다. (최대 힙 구현을 위해 ci대신 -ci를 사용한다.)
- c중 가장 큰 값을 C라 하면 C > N-C+1일 때 즉, (C를 뺀 나머지 c값들의 합)+1보다 C가 크면 보고서대로 시험관을 배열할 수 없다. 왜냐하면 C를 뺀 나머지 시험관들이 규칙대로 배열되어 있다고 할 때 그 집합을 L=N-C이라고 가정한다.(편의상 C와 L의 인덱스(시약 색)도 각각 C, L이라고 명명한다.) C > L+1이면 최소 2개의 C가 서로 이웃하게 되므로 규칙대로 배열하는 것이 불가능하다. L이 규칙대로 배열이 불가능하며, C > N-C+1이면 당연히 규칙대로 배열이 불가능하다.
- 'C > L+1이면 규칙대로 배열이 불가능하다.' 라는 명제의 대우는 '규칙대로 배열이 가능하면 C <= L+1이다.'이다. L이 규칙대로 배열이 불가능한 경우는 앞서 증명했으므로 L이 규칙대로 배열되어 있다고 가정하면, 규칙대로 배열된 L개에 C가 L+1 이하이면 C 사이사이에 L을 넣어 C+L이 규칙대로 배열될 수 있다.
- 따라서 위 증명에 의하여 대우명제가 참이므로 명제 'C > L+1이면 규칙대로 배열이 불가능하다.'도 참이다. 그러므로 C > N-C+1, ```2*C>N+1```이면 규칙대로 배열이 불가능하다.
- 위 경우가 아니면 규칙대로 시험관들을 배열하는 것이 가능하므로 앞서 만들어둔 H에서 heappop하여 각각 ci, i에 저장한다.
    + 만약 이전에 나열한 시약(prev)과 현재 pop된 시약(i)이 같다면 한 번 더 heappop하여 각각 cj, j에 저장한다. j를 출력하고 H에 (cj+1,j)와 (ci,i)를 heappush하고 prev = j한다.
    + 만약 이전에 나열한 시약(prev)과 현재 pop된 시약(i)이 다르다면 i를 출력하고 H에 (ci+1,i)를 heappush하고 prev = i한다.
    + cj+1, ci+1을 heappush하는 이유는 최대힙을 구성하기 위해 c값들이 음수이기 때문이다.
- 위 과정을 N번 반복한다.
---

### 소스코드
- 점수 : 100점
- 메모리 : 66708KB
- 시간 : 924ms
```Python
import sys
import heapq
I = sys.stdin.readline
N, K = map(int, I().split())
H = [(-int(ci), i) for ci, i in zip(I().split(), range(1,K+1))]
heapq.heapify(H)
if -H[0][0]*2 > N+1:
    print(-1)
else:
    prev = 0
    for _ in range(N):
        ci, i = heapq.heappop(H)
        if prev == i:
            cj, j = heapq.heappop(H)
            print(j, end=" ")
            heapq.heappush(H, (cj+1,j))
            heapq.heappush(H, (ci,i))
            prev = j
        else:
            print(i, end=" ")
            heapq.heappush(H, (ci+1,i))
            prev = i
```