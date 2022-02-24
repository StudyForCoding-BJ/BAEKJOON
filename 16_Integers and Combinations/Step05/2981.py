#BOJ 2981
import sys
from math import gcd
n = int(input())
num = []
mag = 1000000000

for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    if tmp < mag:
        mag = tmp
    num.append(tmp)

#minus, gcd
cand = []
for i in range(n-1):
    cand.append(abs(num[i+1]-num[i]))
a = gcd(*cand)

def divisor(n: int):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            res.append(i)
            if i**2 != n:
                op = n//i
                res.append(op)
    res.remove(1)
    return res
print(' '.join(map(str, sorted(divisor(a)))))