def star(x,y,n):
    if n == 1:
        S[x][y] = 1
        return
    for i in range(x,x+n,n//3):
        for j in range(y,y+n,n//3):
            if i==x+n//3 and j==y+n//3:
                continue
            star(i,j,n//3)
n = int(input())
S = [[0]*n for i in range(n)]
star(0,0,n)
for i in range(n):
    for j in range(n):
        if S[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()