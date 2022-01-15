#BOJ 11651 _ 2
#213B, 432ms

import sys
input = sys.stdin.readline

num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: (x[1], x[0]))
for i in data:
    print(*i, sep=' ')