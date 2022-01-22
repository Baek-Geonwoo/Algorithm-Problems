# 백준 1946번 문제
https://www.acmicpc.net/problem/1946
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버I
- 2021.01.14
---

### 접근 방식
- 리스트 A에 지원자의 성적순위들을 저장하고 서류 심사 성적 순위를 기준으로 오름차순으로 정렬
- 우선 서류심사 성적이 제일 높은 사람은 반드시 채용되므로 admit(합격자수 저장 변수)을 1로 초기화하고 그 지원자의 면접 성적 순위를 min_rank(현재까지 가장 낮은 면접 성적 순위 저장 변수)에 저장
- A를 순회할 때 A가 서류 심사 성적 순위를 기준으로 오름차순 정렬되어 있으므로 현재까지 가장 낮은 면접 성적 순위보다 면접 성적 순위가 높아야 선발 가능
- 동석차가 없으므로 A의 인덱스 1부터 n-1까지 순회하면서 min_rank보다 면접 성적 순위가 높은 사람을 선발시키고(admit+=1) 그 사람의 면접 성적 순위로 min_rank를 초기화
---

### 소스코드
- 메모리 : 63532KB
- 시간 : 5760ms
```Python
import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    n = int(I())
    A = [[int(e) for e in I().split()] for _ in range(n)]
    A.sort()
    admit = 1
    min_rank = A[0][1]
    for i in range(1,n):
        if A[i][1]<min_rank:
            admit += 1
            min_rank = A[i][1]
    print(admit)
```