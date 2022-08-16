import sys
input = sys.stdin.readline

N, K = map(int, input().split())
D = [int(e) for e in input().split()]
slot = []
ans = 0

for i, d in enumerate(D):
    if d in slot:
        continue

    if len(slot) < N:
        slot.append(d)
        continue

    slot_idx = []
    for j, s in enumerate(slot):
        if s in D[i:]:
            slot_idx.append(D[i:].index(s))
        else:
            slot_idx.append(101)
            break
    del slot[slot_idx.index(max(slot_idx))]
    slot.append(d)
    ans += 1

print(ans)