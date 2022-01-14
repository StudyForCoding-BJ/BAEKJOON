#BOJ 9020

def era(start, end: int):
    era = [1]*(end+1)
    era[1] = 0

    for i in range(2, int(end**0.5)+1):
        if era[i] == 1:
            for j in range(i*2, end+1, i):
                era[j] = 0

    primelist = []
    for i in range(start, end+1):
        if era[i] == 1:
            primelist.append(i)
    return primelist

for i in range(int(input())):
    even = int(input())
    total = era(2, even)
    for j in range(int(even/2), 1, -1):
        if j in total:
            if even-j in total:
                print (j, even-j)
                break