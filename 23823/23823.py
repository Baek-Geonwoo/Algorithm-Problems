import sys
from collections import defaultdict
def two():
    return map(int, sys.stdin.readline().split())

n, q = two()
cake = [0,defaultdict(int), defaultdict(int)]
MAX = {1:0, 2:0}
cnt = {1:0, 2:0}
for _ in range(q):
    t, a = two()
    cake[t][a] += 1
    if cake[t][a] > MAX[t]:
        MAX[t] = cake[t][a]
        cnt[t] = 1
    elif cake[t][a] == MAX[t]:
        cnt[t] += 1
    if cnt[1]*cnt[2]:
        print(cnt[1]*cnt[2])
    else:
        print((cnt[1]+cnt[2])*n)