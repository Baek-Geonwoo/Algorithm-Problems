# 백준 17298번 오큰수
https://www.acmicpc.net/problem/17298
---

### 문제 해결 날짜
- 2021.03.05
---

### 코드 설명
- ```O[i]에 A[i]의 오큰수를 저장한다. O의 초기값은 '-1'로한다.(오큰수가 없는 경우 오큰수가 -1이므로)```
- stack에 ```A[-1]을 저장한다.(A[-1]은 더이상 오른쪽에 수가 없으므로 오큰수가 -1이므로)```
- 인덱스 N-2부터 0까지 순회하며 다음을 반복한다.
    * ```스택이 비게 되거나, 스택의 가장 위 요소가 A[i]보다 클 때까지 stack의 요소들을 pop한다. while문이 끝나고 stack이 비어있지 않다면 O[i]에 스택의 가장 위의 요소를 저장한다.(stack이 비었으면 오큰수가 존재하지 않는데 O의 초기값이 -1이므로 따로 초기화할 필요가 없다.)```
    * ```stack에 A[i]를 append한다.```
- 각 요소는 모두 stack에 1번씩 append되고, 최대 1번 이하로 pop되므로 시간복잡도는 O(N)이다.
---

### 소스코드
- 메모리 : 159820KB
- 시간 : 1096ms
```Python
import sys
from collections import deque
N, *A = map(int,sys.stdin.read().split())
O = ['-1']*N
stack = deque((A[-1],))
for i in range(N-2,-1,-1):
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack:
        O[i] = str(stack[-1])
    stack.append(A[i])
print(" ".join(O))
```