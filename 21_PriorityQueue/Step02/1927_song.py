# BOJ 1927
# 140ms
# 36784KB

import sys, heapq
input = sys.stdin.readline

# heapq는 최소 힙만 지원
N = int(input())
heap = []

def min_heap():
    for _ in range(N):
        n = int(input())
        if n == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, n)
            
min_heap()