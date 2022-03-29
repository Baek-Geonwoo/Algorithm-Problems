import sys
I = sys.stdin.readline
def wave(S):
    n = len(S)
    i = 0
    while i < n:
        if i == n-1 or S[i] == S[i+1]:
            return 'NO'
        i += 2
        if S[i-2] == '0':
            continue
        if i >= n or S[i] != '0':
            return 'NO'
        i += 1
        while i<n and S[i] == '0':
            i += 1
        if i == n:
            return 'NO'
        while i<n and S[i] == '1':
            i += 1
        if i < n-1:
            if S[i+1] == '1':
                i += 2
            else:
                if S[i-1] == S[i-2] == '1':
                    i -= 1
    return 'YES'

for _ in range(int(I())):
    print(wave(I().strip()))