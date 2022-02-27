import sys
def attack(n):
    for i in range(n):
        if X[i] == X[n]:
            return False
        if X[i]+(n-i) == X[n]:
            return False
        if X[i]-(n-i) == X[n]:
            return False
    return True
def nqueen(cnt):
    global N, ans
    if N == cnt:
        ans += 1
        return
    for i in range(N):
        X[cnt] = i
        if attack(cnt):
            nqueen(cnt+1)
N = int(sys.stdin.readline())
X = [0]*N
ans = 0
nqueen(0)
print(ans)