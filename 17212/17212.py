import sys
n = int(sys.stdin.readline())
P = [e for e in range(n+1)] #P[i]는 i원을 지불하는데 필요한 동전의 최소 개수
coin = [7,5,2]
for c in coin:
    for i in range(2,n+1):
        if c<=i:
            P[i] = min(P[i],P[i-c]+1)
print(P[n])