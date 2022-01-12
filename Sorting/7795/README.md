# 백준 7795번 문제
https://www.acmicpc.net/problem/7795
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버III
- 2021.01.12
---

### 접근 방식
- 재료들 리스트 A를 오름차순 정렬
- A의 인덱스 양 끝을 s와 e에 0, n-1 저장
- s < e인 동안 while문에서 A[s]+A[e]=m이면 s+=1 e-=1 cnt+=1(만들 수 있는 갑옷 수),
- A[s]+A[e]>m이면 초과이므로 e-=1, A[s]+A[e] < m이면 미만이므로 s+=1
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