def solve(n,x,y):
    if n == 0:
        S[x][y] = 1
        return
    solve(n-1,x,y)
    solve(n-1,x+2**(n-1),y)
    solve(n-1,x,y+2**(n-1))

n = int(input())
S = [[0]*2**n for i in range(2**n)]
solve(n,0,0)
for i in range(2**n):
    for j in range(2**n-i):
        if S[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()