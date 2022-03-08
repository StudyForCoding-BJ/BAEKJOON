#BOJ 11401
#n!%p * (k!(n-k)!)^(p-2)%p
import sys

n, k = map(int, input().split())

mod = 1000000007

def pow(a: int, b: int):
    if b == 0:
        return 1
    if b%2 == 0:
        return (pow(a, b//2)**2)%mod
    else:
        return (pow(a, b//2)**2 * a)%mod
    
def factorial(a: int):
    res = 1
    for i in range(1, a+1):
        res = (res*i)%mod
    return res

factn = factorial(n)%mod
factk = (factorial(k)*factorial(n-k))%mod
print((factn*(pow(factk, mod-2)%mod))%mod)