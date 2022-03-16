import sys
I = sys.stdin.readline
T = int(I())
for _ in range(T):
    N = int(I())
    ans = [0]*5
    h, t, o = N//60, (N%60)//10, N%10
    if o > 5:
        t += 1
        o -= 10
    if t > 3:
        h += 1
        t -= 6
    if t < 0 and o == 5:
        t += 1
        o -= 10
    ans[0] = h
    ans[2-(t>0)] = abs(t)
    ans[4-(o>0)] = abs(o)
    print(*ans)