# 백준 11401번 문제
https://www.acmicpc.net/problem/11401
---

### 문제 해결 날짜 및 시간, 문제정보
- 골드I
- 2021.01.04
---

### 접근 방식
- 페르마의 소정리:p가 소수이고 a와p가 서로소이면 a^(p-1)%p=1이다.
- 곱셈의 역원을 이용하면 axa^(p-2)=1(mod p) => a^(p-2)=a-1(mod p)
- P는 a^n을 p(1000000007)로 나눈 나머지를 반환하는 함수
- F[i]에 0~n 까지 i!를 저장
- P에서 P(a,n//2,p)^2*P(a,n%2,p)를 반환한다. n을 계속 반으로 나누어 거듭제곱
- nCk는 n!/(k!*(n-k)!)이고, a^(p-2)=a-1(mod p)이므로 nCk%p=n!%px(k!x(n-k)!)^(p-2)%p이다.
---

### 소스코드
- 메모리 : 185844KB
- 시간 : 1328ms
```Python
def P(a,n,p): #a를 n번 곱한 것을 p로 나눈나머지를 반환하는 함수
    if n == 0:
        return 1
    if n == 1:
        return a
    return (P(a,n//2,p)**2)*(P(a,n%2,p))%p
#1000000007는 소수
#페르마의 소정리
#p가 소수이고 a와p가 서로소이면 a^(p-1)%p=1이다.
n, k = map(int,input().split())
p = 1000000007
F = [1]*(n+1) #F[n]=n!%p
for i in range(2,n+1):
    F[i] = F[i-1]*i%p
print(F[n]*P(F[k]*F[n-k],p-2,p)%p)
```