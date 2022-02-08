import sys
I = sys.stdin.readline
def solve(l):
    global visited
    global S
    global cnt, n
    global ans
    if l == len(S):
        cnt += 1
        if cnt == n:
            print(S,n,"=","".join(ans))
        return
    for i in range(len(S)):
        if visited[i]:
            continue
        ans.append(S[i])
        visited[i] = True
        solve(l+1)
        ans.pop()
        visited[i] = False

while True:
    try:
        S, n = I().strip().split()
    except:
        break
    n = int(n)
    f = 1
    for i in range(2,len(S)+1):
        f *= i
    if n > f:
        print("{} {} = No permutation".format(S, n))
        continue
    visited = [False]*n
    ans = []
    cnt = 0
    solve(0)