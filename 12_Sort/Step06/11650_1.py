#BOJ 11650
#213B, 428ms

import sys
input = sys.stdin.readline

num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x: (x[0], x[1]))
for i in data:
    print(*i, sep=' ')