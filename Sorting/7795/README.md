# 백준 7795번 문제
https://www.acmicpc.net/problem/7795
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버III
- 2021.01.12
---

### 접근 방식
- a와 b를 각각 리스트 A, B의 가장 끝 인덱스로 초기화(a, b는 각각 A, B의 인덱스를 가리킬 포인터)
- A, B를 오름차순 정렬
- A가 B를 먹을 수 있는 쌍의 개수를 cnt에 저장
- a 또는 b가 음수가 되기 전까지 while 루프를 돌면서 다음을 반복
- A[a] > B[b]이면 ~b까지 모든 B들을 A[a]가 먹을 수 있으므로 cnt+=b+1(b는 인덱스이므로 +1)
- A[a] > B[b]가 아니면 A[a]가 B[b]를 먹을 수 없으므로 b -= 1
---

### 소스코드
- 메모리 : 33248KB
- 시간 : 204ms
```Python
import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    n, m = map(int, I().split())
    A = [int(e) for e in I().split()]
    B = [int(e) for e in I().split()]
    A.sort()
    B.sort()
    cnt = 0
    a, b = n-1, m-1
    while a>=0 and b>=0:
        if A[a] > B[b]:
            cnt += b+1
            a -= 1
        else:
            b -= 1
    print(cnt)
```