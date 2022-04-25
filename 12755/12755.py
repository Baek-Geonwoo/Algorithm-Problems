import sys
N = int(sys.stdin.readline())
i = 1
n = 0
while True:
    s = str(i)
    for j in s:
        n += 1
        if n == N:
            print(j)
            sys.exit()
    i += 1