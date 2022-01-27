import sys
I = sys.stdin.readline
N = int(I())
A = [list(map(int,I().split())) for _ in range(N)]
A.sort(key = lambda x: [x[1], x[0]])
curr_time = 0
cnt = 0
for s,e in A:
	if curr_time <= s:
		curr_time = e
		cnt += 1
print(cnt)