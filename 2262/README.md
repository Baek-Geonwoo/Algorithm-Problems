# 백준 2262번 토너먼트 만들기
https://www.acmicpc.net/problem/2262
---

### 문제 해결 날짜
- 2022.05.24
---

### 코드 설명
- 랭킹이 낮은 사람부터 시합을 하는데 그 사람 양옆의 사람 중 랭킹이 더 낮은 사람과 시합을 한다.
- 랭킹이 낮은 사람은 패배하므로 리스트에서 제거한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 72 ms
```Python
import sys
n, *A = map(int, sys.stdin.read().split())
ans = 0
for i in range(n,1,-1):
    idx = A.index(i)
    if idx == len(A)-1:
        ans += A[idx] - A[idx-1]
    elif idx == 0:
        ans += A[idx] - A[idx+1]
    else:
        ans += A[idx] - max(A[idx-1], A[idx+1])
    A.pop(idx)
print(ans)
```
---

### 오답 노트
- 틀렸습니다.
- 랭킹 차이가 작은 사람들부터 경기시켰다.
- 랭킹 차이가 작은 사람들부터 경기시키면 그 다음 경기부터는 랭킹 차이가 점점 증가한다.

### 오답 코드
```Python
import sys
n, *A = map(int, sys.stdin.read().split())
ans = 0
for _ in range(n-1):
    min_idx = 0
    min_diff = n+1
    for i in range(len(A)-1):
        if abs(A[i]-A[i+1]) < min_diff:
            min_idx = i
            min_diff = abs(A[i]-A[i+1])
    ans += min_diff
    A.insert(min_idx, min(A[min_idx], A[min_idx+1]))
    del A[min_idx+1], A[min_idx+1]
print(ans)
```