import sys
I = sys.stdin.readline
N = int(I())
M = [[int(e) if e.isdigit() else e for e in list(I().strip())] for _ in range(N)]
ans = max(N-4,0)**2
d = (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)
for x in range(1,N-1):
    for y in (1,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
for x in (1,N-2):
    for y in range(2,N-2):
        zero = 0
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] == 0:
                zero = 1
                break
        if zero:
            continue
        ans += 1
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if M[nx][ny] != '#':
                M[nx][ny] -= 1
print(ans)