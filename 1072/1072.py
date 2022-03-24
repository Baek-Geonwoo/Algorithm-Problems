import sys
def check(M):
    if (Y+M)*100//(X+M) != Z:
        return True
    return False
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X
if Z >= 99:
    print(-1)
else:
    low, high = 0, 10**9
    while low+1 < high:
        mid = (low + high)//2
        if check(mid): high = mid
        else: low = mid
    print(high)