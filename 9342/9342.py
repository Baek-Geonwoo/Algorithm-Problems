import sys
import re
def input():
    return sys.stdin.readline().strip()
def DNA(S):
    return re.fullmatch('[A-F]{0,1}A+F+C+[A-F]{0,1}', S)
for _ in range(int(input())):
    if DNA(input()):
        print("Infected!")
    else:
        print("Good")