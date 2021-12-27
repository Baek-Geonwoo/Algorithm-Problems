def sol(pos,num):
    global ans
    if pos == -1:
        if '0' not in str(num):
            ans = max(ans, num)
        return
    for i in range(k):
        curr = A[i]*10**pos+num
        if curr <= n:
            sol(pos-1, curr)
        else:
            sol(pos-1, num)

n, k = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = 0
sol(len(str(n))-1,0)
print(ans)