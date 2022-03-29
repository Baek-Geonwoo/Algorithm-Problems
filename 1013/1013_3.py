import sys, re
I = sys.stdin.readline
for _ in range(int(I())):
    print('YES') if re.fullmatch('(100+1+|01)+',I().strip()) else print('NO')