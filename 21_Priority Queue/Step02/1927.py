#BOJ 1927
#heapq - min heap
#36784KB, 152ms
import heapq
import sys
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
        heapq.heappush(x, tmp)