# 백준 16112번 문제
https://www.acmicpc.net/problem/16112
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버II
- 2021.01.13
---

### 접근 방식
- exp에는 경험치 저장 / cnt에는 현재 활성화 된 아케인스톤의 수
- A에는 각 퀘스트를 끝내면 주는 경험치들을 저장, 오름차순으로 정렬
- 퀘스트를 진행했을 때 활성화 된 아케인스톤의 수 x 퀘스트 보상 경험치 만큼 아케인스톤에 경험치가 저장되므로 경험치를 적게 주는 퀘스트부터 진행하고 아케인스톤을 받아서 활성화
- i번째 퀘스트를 끝내먄 cnt x A[i] 만큼의 경험치가 아케인스톤들에 저장됨
- 단, cnt는 k를 초과할 수 없으므로 cnt는 루프를 돌 때마다 cnt+1과 k중 작은 값으로 업데이트
---

### 소스코드
- 메모리 : 65852KB
- 시간 : 384ms
```Python
import sys
I = sys.stdin.readline
n, k = map(int, I().split())
A = [int(e) for e in I().split()]
exp = 0 #경험치
cnt = 0 #현재 활성화된 아케인스톤의 수
A.sort()
for i in range(n):
    exp += cnt*A[i]
    cnt = min(cnt+1,k)
print(exp)
```