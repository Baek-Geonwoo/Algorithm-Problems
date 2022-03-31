import sys, re
print("SUBMARINE") if re.fullmatch('(100+1+|01)+',sys.stdin.readline().strip()) else print("NOISE")