#BOJ 11651 _ 1
#199B, 428ms

import sys

num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x: (x[1], x[0]))
for i in data:
    print(*i, sep=' ')