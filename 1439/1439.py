import sys
S = sys.stdin.readline().rstrip('\n')
num = {'0':0, '1':0}
prev = S[0]
num[S[0]] += 1
for i in range(1,len(S)):
    if S[i] != prev:
        num[S[i]] += 1
        prev = S[i]
if num['0'] + num['1'] == 1:
    print(0)
else:
    print(min(num['0'], num['1']))