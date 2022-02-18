import sys
sys.stdin.readline()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))