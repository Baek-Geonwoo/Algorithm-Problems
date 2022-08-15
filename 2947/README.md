# 백준 2947번 나무 조각
https://www.acmicpc.net/problem/1072
---

### 문제 해결 날짜
- 2022.08.15
---

### 코드 설명
- 입력받은 리스트가 오름차순 정렬이 될 때까지 문제의 과정을 반복한다.
- 위치가 변경될 때만 현재 상태를 출력한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 88 ms
```Python
import sys
input = sys.stdin.readline
L = [int(e) for e in input().split()]

while L != [1,2,3,4,5]:
    for i in range(4):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
            print(*L)
```