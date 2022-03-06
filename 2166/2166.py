import sys
I = sys.stdin.readline
N = int(I())
ans = 0
sx, sy = map(int, I().split())
px, py = map(int, I().split())
for i in range(N-2):
    cx, cy = map(int, I().split())
    ans += ((px-sx)*(cy-sy)-(py-sy)*(cx-sx))/2
    px, py = cx, cy
print("%.1f" %abs(ans))