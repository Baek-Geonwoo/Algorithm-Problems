import sys
n, d = map(int,sys.stdin.readline().split())
ans = 0
for i in range(1,n+1):
    ans += str(i).count(str(d))
print(ans)