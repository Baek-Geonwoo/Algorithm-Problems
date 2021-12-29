import sys
input = sys.stdin.readline
n = int(input())
paper = [[int(e) for e in input().split()] for i in range(n)]
p = [0,0] #순서대로 하얀색 파란색
def solve(x,y,e):
    color = paper[x][y]
    for i in range(x,x+e):
        for j in range(y,y+e):
            if color != paper[i][j]:
                solve(x,y,e//2)
                solve(x+e//2,y,e//2)
                solve(x,y+e//2,e//2)
                solve(x+e//2,y+e//2,e//2)
                return
    p[color] += 1
    return
solve(0,0,n)
for i in range(2):
    print(p[i])