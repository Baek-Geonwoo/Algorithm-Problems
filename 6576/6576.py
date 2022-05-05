def solve(x,y,size):
    global idx
    if S[idx] == "Q":
        size //= 2
        idx += 1
        solve(x,y,size)
        solve(x,y+size,size)
        solve(x+size,y,size)
        solve(x+size,y+size,size)
    else:
        if S[idx] == "B":
            for i in range(x,x+size):
                for j in range(y,y+size):
                    Q[i][j] = 1
        idx += 1
n = int(input())
S = input()
Q = [[0]*n for i in range(n)]
idx = 0
solve(0,0,n)
print("#define quadtree_width", n)
print("#define quadtree_height", n)
print("static char quadtree_bits[] = {")
for i in range(n):
    for j in range(n//8):
        b = 0 #비트값의 지수 2^b
        bit = 0 #비트값
        for k in range(j*8,(j+1)*8):
            bit += Q[i][k]*2**b
            b += 1
        print('{:#04x}'.format(bit),end=",")
    print()
print("};")