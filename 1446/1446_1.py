import sys
input = sys.stdin.readline
N, D = map(int, input().split())
distance = [0]*(D+1)
shortcut = {}

for _ in range(N):
    s, e, d = map(int, input().split())
    if e <= D:
        if shortcut.get(e) == None:
            shortcut[e] = []
        shortcut[e].append((s,d))

for i in range(1,D+1):
    distance[i] = distance[i-1]+1
    if shortcut.get(i) != None:
        for s, d in shortcut[i]:
            distance[i] = min(distance[i], distance[s]+d)
print(distance[D])