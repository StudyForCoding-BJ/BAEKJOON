#BOJ 11050 _ 2
#32976KB, 76ms
from math import factorial
n, k = map(int, input().split())
print(factorial(n)//factorial(k)//factorial(n-k))