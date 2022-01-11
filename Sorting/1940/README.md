# 백준 1940번 문제
https://www.acmicpc.net/problem/1940
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버IV
- 2021.01.11
---

### 알고리즘 분류
- 정렬
- 투 포인터
---

### 접근 방식
- 재료들 리스트 A를 오름차순 정렬
- A의 인덱스 양 끝을 s와 e에 0, n-1 저장
- s < e인 동안 while문에서 A[s]+A[e]=m이면 s+=1 e-=1 cnt+=1(만들 수 있는 갑옷 수),
- A[s]+A[e]>m이면 초과이므로 e-=1, A[s]+A[e] < m이면 미만이므로 s+=1
---

### 소스코드
- 메모리 : 31880KB
- 시간 : 80ms
```Python
import sys
I = sys.stdin.readline
n = int(I())
m = int(I())
A = [int(e) for e in I().split()]
A.sort()
s,e = 0, n-1
cnt = 0
while s < e:
    if A[s]+A[e] == m:
        cnt += 1
        s += 1
        e -= 1
    elif A[s]+A[e] < m:
        s += 1
    else:
        e -= 1
print(cnt)
```