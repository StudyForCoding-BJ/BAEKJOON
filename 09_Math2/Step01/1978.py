#BOJ 1978
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

num = int(input())
given = input().split()
for i in range(num):
    given[i] = isPrime(int(given[i]))
print (given.count(1))