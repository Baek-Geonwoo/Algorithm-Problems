# 백준 19942번 다이어트
https://www.acmicpc.net/problem/19942
---

### 문제 해결 날짜
- 2022.05.13
---

### 코드 설명
- combination을 통해 `1~N`개의 재료 묶음 조합을 모두 구하여 해당 조합의 영양성분이 최소영양성분 이상이고 현재까지 구한 최소비용 미만의 비용이 들면 ans, ans_lst를 초기화한다.(ans는 최소비용, ans_lst는 최소비용조합의 재료 번호리스트)
- v_sum, v_sub, v_boolean은 numpy 기능을 리스트에서 구현하기 위한 함수이다.
    * v_sum (numpy +연산 or numpy.sum(array, axis=0) 구현)
    * v_sub (numpy -연산 구현)
    * v_boolean (numpy boolean 연산 구현)
---

### 소스코드
- 메모리 : 31860KB
- 시간 : 364ms
```Python
import sys
from itertools import combinations
def v_sum(V, l=0, r=3, C=[]):
    ret = [0]*(r+1)
    if not C:
        for v in V:
            for i in range(l,r+1):
                ret[i] += v[i]
        return ret
    else:
        for c in C:
            for i in range(l,r+1):
                ret[i] += V[c][i]
        return ret
def v_sub(V, W):
    return [v-w for v, w in zip(V,W)]
def v_boolean(V):
    return sum([v>=0 for v in V])
    
input = sys.stdin.readline
N = int(input())
m = list(map(int, input().split()))
I = [list(map(int, input().split())) for _ in range(N)]
if v_boolean(v_sub(v_sum(I),m))!=4:
    print(-1)
else:
    ans = 500*N
    ans_lst = []
    for i in range(1,N+1):
        for c in list(combinations(range(N), i)):
            if v_boolean(v_sub(v_sum(I,0,3,c),m))==4:
                cost = v_sum(I,4,4,c)[4]
                if cost < ans:
                    ans = cost
                    ans_lst = list(c)
                elif cost == ans:
                    if ans_lst > list(c):
                        ans_lst = list(c)
    print(ans)
    print(*v_sub(ans_lst,[-1]*len(ans_lst)))
```
---

### 오답 노트
- 런타임 에러 (ModuleNotFoundError)
- BOJ에서는 numpy를 쓸 수 없다는 것을 알게 되었다.

### 오답 코드
```Python
import sys
import numpy as np
from itertools import combinations
input = sys.stdin.readline
N = int(input())
m = np.array(list(map(int, input().split())))
I = np.array([np.array(list(map(int, input().split()))) for _ in range(N)])
if sum(np.sum(I[:,:-1], axis=0)-m>=0)!=4:
    print(-1)
else:
    ans = 500*N
    ans_lst = []
    for i in range(1,N+1):
        for c in list(combinations(range(N), i)):
            if sum(np.sum(I[c,:-1], axis=0)-m>=0)==4 and ans > np.sum(I[c,-1]):
                ans = np.sum(I[c,-1])
                ans_lst = np.array(list(c))
    print(ans)
    print(*ans_lst+1)
```