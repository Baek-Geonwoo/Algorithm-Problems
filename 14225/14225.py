import sys
def dfs(i, Sum):
    if i == N:
        return
    num.add(Sum)
    dfs(i+1, Sum)
    num.add(Sum+S[i])
    dfs(i+1, Sum+S[i])

N, *S = map(int, sys.stdin.read().split())
num = set()
dfs(0,0)
n = 1
while True:
    if n not in num:
        print(n)
        break
    n += 1