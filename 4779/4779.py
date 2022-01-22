import sys
input = sys.stdin.readline
def solve(n,x):
    if n == 0:
        return
    solve(n-1,x)
    for i in range(x+3**(n-1),x+2*3**(n-1)):
        C[i] = " "
    solve(n-1,x+2*3**(n-1))
while True:
    try:
        n = input()
        n = int(n)
        C = ["-"]*3**n
        solve(n,0)
        print("".join(C))
    except:
        break