import sys
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def is_in(x,y):
    if 0<=x<5 and 0<=y<5:
        return True
    return False

def solution(x,y):
    if len(ans) == 6:
        S = "".join(ans)
        Set.add(S)
        return
    for i in range(4):
        X, Y = x+dx[i], y+dy[i]
        if is_in(X, Y):
            ans.append(A[X][Y])
            solution(X, Y)
            ans.pop()

I = sys.stdin.readline
A = [I().split() for _ in range(5)]
Set = set()
for x in range(5):
    for y in range(5):
        ans = [A[x][y]]
        solution(x, y)
print(len(Set))