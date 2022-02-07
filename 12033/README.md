# 백준 12033번 김인천씨의 식료품가게 (Small)
https://www.acmicpc.net/problem/12033
---

### 문제 해결 날짜
- 2021.02.07
---

### 접근 방식
- 정가와 할인가가 오름차순으로 정렬된 리스트 A에서 ```A[0]은 반드시 할인가 이므로 A[0]*4//3인 A[0]에 해당하는 정가(A[i]라 가정)를 A를 순회하며 찾아(찾으면 break) A[0], A[i]를 N번 pop한다.```
---

### 소스코드
- 메모리 : 30860KB
- 시간 : 64ms
```Python
import sys
I = sys.stdin.readline
T = int(I())
for t in range(1,T+1):
    N = int(I())
    A = [int(e) for e in I().split()]
    D = []
    for _ in range(N):
        d = A[0]
        D.append(A[0])
        A.pop(0)
        for i in range(len(A)):
            if A[i] == d*4//3:
                A.pop(i)
                break
    print("Case #{}: ".format(t)+" ".join(map(str,D)))
```