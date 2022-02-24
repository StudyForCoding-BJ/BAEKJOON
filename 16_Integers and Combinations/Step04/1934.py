#BOJ 1934
import math
import sys
n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))