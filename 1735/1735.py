import sys
from math import gcd
I = sys.stdin.readline
F = [list(map(int,I().split())) for _ in range(2)]
fn, fd = 0, 1
for i in range(2):
    fn += F[i][0] * F[(i+1)%2][1]
    fd *= F[i][1]
g = gcd(fn,fd)
print(fn//g, fd//g)