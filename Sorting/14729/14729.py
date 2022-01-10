import sys
input = sys.stdin.readline
n = int(input())
seven = []
for i in range(n):
    seven.append(float(input()))
    if len(seven) > 7:
        seven.sort()
        seven.pop()
for i in range(7):
    print("%.3f" %seven[i])