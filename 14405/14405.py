import sys
import re
if re.fullmatch('(pi|ka|chu)+', sys.stdin.readline().strip()):
    print("YES")
else: print("NO")