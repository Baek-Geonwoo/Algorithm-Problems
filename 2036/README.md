# 백준 2036번 문제
https://www.acmicpc.net/problem/2036
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버I
- 2021.01.14
---

### 접근 방식
- 리스트 A에 정수들을 저장하고 오름차순으로 정렬
+ 음수 부분
    - i=0(인덱스 저장 변수)부터 시작해서 i가 증가하며 절댓값이 큰 음수부터 2개씩 곱하여 점수에 더함
    - 만약 음수가 홀수개면 두 가지 경우로 나뉨
        * A에 0이 존재하는 경우는 마지막 음수x0=0 이므로 점수변동x
        * A에 0이 존재하지 않으면 점수에 마지막 음수를 더함
+ 양수 부분
    - i=n-1(인덱스 저장 변수)부터 시작해서 i가 감소하며 큰 수부터 2개씩 곱하여 점수에 더함
        * 단, 두 수중 하나 이상이 1이면 두 수를 곱한 것보다 더한 것이 더 크므로 두 수를 더한 것을 점수에 더함
    - 양수가 홀수개인 경우 마지막 수(A에서 가장 작은 양수)를 정수에 더하고 while 루프 종료
- 각 경우 모두 현재 위치 인덱스와 그 인덱스 보다 한칸 앞이나 뒤도 사용하므로 Index Error가 발생할 수 있으므로 예외처리 사용
---

### 소스코드
- 메모리 : 35104KB
- 시간 : 156ms
```Python
import sys
I = sys.stdin.readline
n = int(I())
A = []
for _ in range(n):
    A.append(int(I()))
A.sort()
i = 0
score = 0
while i<n:
    if A[i]<0:
        try:
            if A[i+1]<0:
                score += A[i]*A[i+1]
                i += 2
            elif A[i+1]==0:
                break
            else:
                score += A[i]
                break
        except:
            score += A[i]
            break
    else:
        break
i = n-1
while 0<=i:
    if A[i]>0:
        try:
            if A[i-1]>0:
                score += max(A[i]*A[i-1],A[i]+A[i-1])
                i -= 2
            else:
                score += A[i]
                break
        except:
            score += A[i]
            break
    else:
        break
print(score)
```