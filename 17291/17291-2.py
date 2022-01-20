import sys
n = int(sys.stdin.readline())
P = [0]*21 #P[i]는 i년 말의 생존개체 수
P[0]=1
P[1]=1
for i in range(2,n+1):
    if i%2:
        P[i] = P[i-1]*2
    else:
        P[i] = P[i-1]*2 - P[i-4] - P[i-5]
print(P[n])