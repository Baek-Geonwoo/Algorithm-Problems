import sys
def star(n):
    if n == 3:
        return ['***','* *','***']
    ret = []
    S = star(n//3)
    for s in S:
        ret.append(s*3)
    for s in S:
        ret.append(s+' '*(n//3)+s)
    for s in S:
        ret.append(s*3)
    return ret
n = int(input())
print('\n'.join(star(n)))