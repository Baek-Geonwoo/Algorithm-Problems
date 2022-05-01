# 백준 1484번 다이어트
https://www.acmicpc.net/problem/1484
---

### 문제 해결 날짜
- 2022.05.01
---

### 코드 설명
- 현재 몸무게를 e 이전 몸무게를 s라 하면 e^2-s^2=(e+s)(e-s)=G이다.
- 따라서 G의 약수를 axb쌍으로 구했을 때 a+b = 2e이므로 다음 조건을 만족하면 e를 구하여 출력한다. a, b = n, G//n
    * G%n==0 (e는 정수이므로)
    * (n+G//n)%2 == 0 (e는 정수이므로)
    * n != G//n (n == G//n이면 a==b인데 그러면 s가 0이 되어야 하고 이는 모순이므로)
- 만약 한번도 e가 출력되지 않았다면 가능한 몸무게가 없으므로 -1을 출력한다.
---

### 소스코드
- 메모리 : 30840 KB
- 시간 : 68 ms
```Python
import sys
G = int(sys.stdin.readline())
flag = 1
for n in range(int(G**0.5),0,-1):
    if G%n==0 and (n+G//n)%2 == 0 and n!=G//n:
        print((n+G//n)//2)
        flag = 0
if flag: print(-1)
```