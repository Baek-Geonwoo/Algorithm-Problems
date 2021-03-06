# 백준 1052번 물병
https://www.acmicpc.net/problem/1052
---

### 문제 해결 날짜
- 2021.01.28
---

### 접근 방식
- N을 2진수로 바꾼 문자열을 B라고 한다. (ex: N=3이면 B='11')
- B에서 1이 물이 담긴 물병이고, 그 물병에는 자리수만큼 물이 들어있다.
    * ex: B=101이면 물이 담긴 물병은 2개이고, 각각 2^2=4, 2^0=1, 4리터와, 1리터의 물이 담겨 있다.
- 그리디 기준 : B에서 가장 작은 자리수의 1부터 제거한 후 B를 업데이트한다. (새로운 물병을 사서 다른 물병에 옮겨 담아 물이 들어 있는 물병의 수를 줄인다.)
    * ex: B=10011이고, K=2면 10011 -> 10100
- B의 1의 개수가 K보다 작거나 같을 때까지 B에서 오른쪽(자리수가 작은 쪽)부터 1을 제거한다. 이 때 특정 자리수의 1을 제거할 때 사야 하는 물병의 수는 그 자리수만큼이다.
    * ex: B=1100100에서 가장 오른쪽의 1을 제거할 때 그 1의 자리수는 2^2자리이므로 4개의 물병을 사야 한다.
---

### 소스코드
- 메모리 : 30864KB
- 시간 : 76ms
```Python
import sys
N, K = map(int, sys.stdin.readline().split())
#이진수로 바꿨을 때 1의 수가 물병의 수
#그리디 기준: 이진수의 1의 개수가 K보다 클 때 작은 자리의 1부터 소거
buy = 0
B = format(N, 'b')
if B.count('1') <= K:
    print(buy)
else:
    i = 1
    while B.count('1') > K:
        if B[-i] == '1':
            B = format(int(B,2)+2**(i-1), 'b')
            buy += 2**(i-1)
        i += 1
    print(buy)
```