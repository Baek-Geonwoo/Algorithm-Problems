# 백준 14729번 칠무해
https://www.acmicpc.net/problem/14729
---

### 문제 해결 날짜 및 시간, 문제정보
- 실버V
- 2022.01.10
---

### 접근 방식
- 리스트 seven에 하위 7명의 점수를 저장
- 점수들을 입력받으면서 seven의 크기가 7이하일 때는 계속 입력받고, seven의 크기가 7초과일 경우 seven을 정렬한 후 최고점수를 pop하여 최종적으로 하위 7명의 점수가 seven에 오름차순으로 저장
- 소수점 이하 3자리까지 하위 7명의 점수를 오름차순으로 출력
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 5276ms
```Python
import sys
input = sys.stdin.readline
n = int(input())
seven = []
for i in range(n):
    seven.append(float(input()))
    if len(seven) > 7:
        seven.sort()
        seven.pop()
for i in range(7):
    print("%.3f" %seven[i])
```