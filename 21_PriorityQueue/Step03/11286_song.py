# BOJ 11286
# 156ms
# 39564KB

import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

def abs_heap():
    for _ in range(N):
        n = int(input())
        if n != 0:
            # 음수일 경우 양수로 바꿔줌 -> 가짜 우선순위를 기준으로 최소 힙 구성
            heapq.heappush(heap, (abs(n), n))     
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0) 

abs_heap()