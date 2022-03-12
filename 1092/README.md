# 백준 1092번 배
https://www.acmicpc.net/problem/1092
---

### 문제 해결 날짜
- 2021.03.12
---

### 코드 설명
- 만약 무게 제한이 가장 큰 크레인보다 무거운 박스가 있다면 모든 박스를 옮기는 것이 불가능하므로 -1을 출력한다.
- 크레인 리스트와 박스 무게 리스트를 내림차순으로 정렬한다.
- 무게 제한이 가장 큰 크레인부터, 현재 옮길 수 있는 가장 무거운 박스부터 옮긴다.
- ```pos[i]는 C[i]가 마지막으로 옮긴 박스의 위치+1(초기값은 0)```, ```moved[i]는 B[i]가 옮겨졌는지 여부를 저장```
- cnt(옮긴 박스 수)가 M이 될 때까지 크레인을 순회하는 것을 반복하며 옮길 수 있는 박스를 찾을 떄까지 while문을 돌며 ```pos[i]를 체크하고, 찾으면 해당 moved[pos[i]]=1```
- 시간복잡도 : ```O(N*M^2)```
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 328ms
```Python
import sys
I = sys.stdin.readline
N = int(I())
C = [int(e) for e in I().split()]
M = int(I())
B = [int(e) for e in I().split()]
if max(C) < max(B):
    print(-1)
else:
    C.sort(reverse=True)
    B.sort(reverse=True)
    pos = [0]*N
    moved = [0]*M
    cnt = 0
    ans = 0
    while cnt<M:
        for i in range(N):
            while pos[i] < M:
                if not moved[pos[i]] and B[pos[i]] <= C[i]:
                    moved[pos[i]] = 1
                    pos[i] += 1
                    cnt += 1
                    break
                pos[i] += 1
        ans += 1
    print(ans)
```