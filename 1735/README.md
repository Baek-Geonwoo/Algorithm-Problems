# 백준 1735번 분수  
https://www.acmicpc.net/problem/1735
---

### 문제 해결 날짜
- 2021.03.04
---

### 코드 설명
- 두 분수의 분자, 분모를 각각 a,b, c,d라 할때 두 분수의 합이 되는 분수의 분자 분모는 각각 ```fn = a*d+c*d, fd = b*d```이고, 이를 기약분수로 만들기 위해 분자, 분모를 fn, fd의 최대공약수로 나눈다.
---

### 소스코드
- 메모리 : 32976KB
- 시간 : 80ms
```Python
import sys
from math import gcd
I = sys.stdin.readline
F = [list(map(int,I().split())) for _ in range(2)]
fn, fd = 0, 1
for i in range(2):
    fn += F[i][0] * F[(i+1)%2][1]
    fd *= F[i][1]
g = gcd(fn,fd)
print(fn//g, fd//g)
```