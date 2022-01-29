import sys
N = int(sys.stdin.readline())
s, e = 1, 1
S = 0
cnt = 0
while s <= e and s <= N:
    if S < N:
        if e > N:
            S += e
            e += 1
        else:
            break
    elif S > N:
        S -= s
        s += 1
    else:
        cnt += 1
        if e <= N:
            S -= s
            s += 1
        else:
            break
print(cnt)