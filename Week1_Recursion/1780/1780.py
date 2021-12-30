import sys
input = sys.stdin.readline
def solve(x,y,n):
    if n == 1:
        D[P[x][y]] += 1
        return
    is_same = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if P[x][y] != P[i][j]:
                is_same = False
                break
    if is_same:
        D[P[x][y]] += 1
    else:
        for i in range(3):
            for j in range(3):
                solve(x+i*(n//3),y+j*(n//3),n//3)
n = int(input())
P = [input().rstrip('\n').split() for _ in range(n)]
D = {'-1':0,'0':0,'1':0}
solve(0,0,n)
for i in range(-1,2):
    print(D[str(i)])