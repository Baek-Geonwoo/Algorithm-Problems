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