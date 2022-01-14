#BOJ 2581

import math

def isPrime(a: int):
    divBy = 1
    if a == 1:
        return 0
    while divBy <= math.sqrt(a):
        if a%divBy != 0:
            divBy += 1
        elif a%divBy == 0 and a/divBy == a:
            divBy += 1
        else:
            return 0
    return 1

minimum = int(input())
maximum = int(input())
primelist = []
for i in range(minimum, maximum+1):
    if isPrime(i) == 1:
        primelist.append(i)
    else:
        continue
if len(primelist) == 0:
    print(-1)
else:
    print (sum(primelist), primelist[0], sep='\n')