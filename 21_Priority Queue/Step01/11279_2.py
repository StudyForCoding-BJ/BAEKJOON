#BOJ 11279 _ 2
#heapq 구현
#46000KB, 180ms
#priority queue보다 heapq가 더 빠름
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
        heapq.heappush(x, (-tmp, tmp))