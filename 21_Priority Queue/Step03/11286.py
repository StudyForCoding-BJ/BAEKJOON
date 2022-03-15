#BOJ 11286
#heapq
#39564KB, 168ms
import sys
import heapq
input = sys.stdin.readline

n = int(input())
x = []

for i in range(n):
    tmp = int(input())
    if tmp == 0:
        if len(x) == 0:
            print(0)
        else:
            print(heapq.heappop(x)[1])
    else:
        heapq.heappush(x, (abs(tmp), tmp))