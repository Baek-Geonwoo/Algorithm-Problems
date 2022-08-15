import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
ans = 0
polygon = [[int(e) for e in input().split()] for _ in range(N)]

for a,b,c in combinations(polygon, 3):
    triangle = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    triangle -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    triangle = abs(triangle)/2
    ans = max(ans, triangle)
print(ans)