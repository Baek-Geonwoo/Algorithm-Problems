import sys
def check(w):
    X, Y = pow(x**2-w**2,0.5), pow(y**2-w**2,0.5)
    if c <= X*Y/(X+Y):
        return True
    return False
x, y, c = map(float,sys.stdin.readline().split(" "))
lo, hi = 0, min(x,y)
while lo+0.001<hi:
    mid = (lo+hi)/2
    if check(mid): lo = mid
    else: hi = mid
print("%.3f"%hi)