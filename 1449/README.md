# 백준 1449번 수리공 항승
https://www.acmicpc.net/problem/1449
---

### 문제 해결 날짜
- 2021.02.12
---

### 접근 방식
- 왼쪽에서부터 가장 가까운 테이프가 안붙여진 새는 곳부터 테이프를 붙인다.
- 새는 곳의 위치들이 저장된 리스트 A를 오름차순 정렬하고 사용한 테이프 개수 ans와 가장 마지막에 붙인 테이프의 오른쪽 끝 위치 pos를 0으로 초기화한다.
- A의 요소들을 a로 순회하면서 pos < a 일때(테이프가 새는 곳 a에 붙여지지 않았을 때) 테이프를 하나 더 붙이므로 ans += 1, pos = a+L-1한다.(새는 곳 양끝 0.5만큼 간격을 주어야 하므로 a+L에서 -1한다.)
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 72ms
```Python
import sys
I = sys.stdin.readline
N, L = map(int, I().split())
A = [int(e) for e in I().split()]
A.sort()
pos = 0
ans = 0
for a in A:
    if pos < a:
        ans += 1
        pos = a+L-1
print(ans)
```