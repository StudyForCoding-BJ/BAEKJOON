#BOJ 1010
from math import comb
import sys
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(comb(b, a))