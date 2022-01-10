#BOJ 2775

def floor(a, b: int):
    fl = list(range(1,b+1))
    pplfl = [0]*b
    num = 1
    while num <= a:
        for i in range(len(fl)):
            ppl = 0
            for j in range(0, i+1):
                ppl += fl[j]
            pplfl[i] = ppl
        num += 1
        for i in range(len(fl)):
            fl[i] = pplfl[i]
    return fl[b-1]

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print (floor(k,n))