import sys
I = sys.stdin.readline
n, k = map(int, I().split())
A = [int(e) for e in I().split()]
exp = 0 #경험치
cnt = 0 #현재 활성화 된 아케인스톤의 수
A.sort()
for i in range(n):
    exp += cnt*A[i]
    cnt = min(cnt+1,k)
print(exp)