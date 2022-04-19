import sys
I = sys.stdin.readline
t = int(I())
for _ in range(t):
    n, K = map(int, I().split())
    A = [int(e) for e in I().split()]
    A.sort()
    diff = 200000000
    ans = 0
    for i in range(n):
        low, high = i+1, n-1
        while low <= high:
            m = (low + high)//2
            S = A[i]+A[m] 
            if S == K:
                if diff == 0:
                    ans += 1
                else:
                    diff = 0
                    ans = 1
                break
            elif S > K:
                high = m-1
            else:
                low = m+1
            if diff == abs(S-K):
                ans += 1
            elif diff > abs(S-K):
                ans = 1
                diff = abs(S-K)
    print(ans)