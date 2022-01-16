import sys
I = sys.stdin.readline
n, m = map(int,I().split())
d, hd = "", 0 #각각 Hamming Distance가 최소인 DNA 문자열과 그 값
D = [I().rstrip('\n') for _ in range(n)]
for i in range(m):
    DNA = {'A':0, 'T':0, 'G':0, 'C':0}
    for j in range(n):
        DNA[D[j][i]] += 1
    dna = []
    for j in DNA.keys():
        dna.append([DNA[j],j])
    dna.sort(reverse=True, key= lambda x: (x[0], -ord(x[1])))
    d += dna[0][1]
    hd += (n-dna[0][0])
    print(dna)
print(d)
print(hd)