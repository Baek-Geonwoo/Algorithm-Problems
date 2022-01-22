import sys
input = sys.stdin.readline
def solve(x,y,n):
    if n == 1:
        return Q[x][y]
    isSame = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if Q[x][y] != Q[i][j]:
                isSame = False
                break
    if isSame:
        return Q[x][y]
    return '('+solve(x,y,n//2)+solve(x,y+n//2,n//2)+solve(x+n//2,y,n//2)+solve(x+n//2,y+n//2,n//2)+')'
n = int(input())
Q = [list(input().rstrip('\n')) for _ in range(n)]
print(solve(0,0,n))