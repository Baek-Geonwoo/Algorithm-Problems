import sys
def get_exp(limit,e):
    b = e
    ans = 0
    while b <= limit:
        ans += limit//b
        b *= e
    print(ans)
    return ans
n, m = map(int, sys.stdin.readline().split())
ans = [get_exp(n,2), get_exp(n,5)]
for x in (m,n-m):
    for i,e in enumerate((2,5)):
        ans[i] -= get_exp(x,e)
print(min(ans))