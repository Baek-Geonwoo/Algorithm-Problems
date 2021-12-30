def solve(n,x):
    if n == 0:
        return max(n,x)
    if B[n]-n<=x: #레벨 n버거의 맨위는 n개 이상의 버거 번이 있으므로
        return P[n]
    if n>=x: #레벨 n버거의 맨 아래는 n개 이상의 버거 번이 있으므로
        return 0
    if x <= B[n-1]+1:
        return solve(n-1,x-1)
    elif x == 1+B[n-1]+1:
        return 1+P[n-1]
    elif x > 1+B[n-1]+1:
        return solve(n-1,x-1-B[n-1]-1)+1+P[n-1]

n, x = map(int,input().split())
P = [0]*51
B = [0]*51
P[0], B[0] = 1, 1
for i in range(1,n+1):
    P[i] = P[i-1] + 1 + P[i-1]
    B[i] = 1+ B[i-1] + 1 + B[i-1] + 1
print(solve(n,x))