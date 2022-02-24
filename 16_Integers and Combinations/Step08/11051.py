#BOJ 11051 _ lib
#32976KB, 76ms
from math import comb
n, k = map(int, input().split())
print(comb(n, k)%10007)