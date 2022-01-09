#9020

#BOJ 9020

def era(start, end: int):
    era = [1]*(end+1)
    era[1] = 0

    for i in range(2, int(end**0.5)+1):
        if era[i] == 1:
            for j in range(i*2, end+1, i):
                era[j] = 0

    return era

for i in range(int(input())):
    even = int(input())
    total = era(1, even)
    a = even//2
    b = a
    for j in range(even):
        if total[a]==1 and total[b] == 1:
            print(a,b)
            break
        a -= 1
        b += 1