#BOJ 1655
#다른 풀이 참조
import sys
import heapq
input = sys.stdin.readline

n = int(input())
lhp = []
rhp = []

for i in range(n):
    tmp = int(input())
    if len(lhp) == len(rhp):
        heapq.heappush(lhp, -tmp)
    else:
        heapq.heappush(rhp, tmp)
    
    if len(lhp) != 0 and len(rhp) != 0:
        if -lhp[0] > rhp[0]:
            left = -heapq.heappop(lhp)
            right = heapq.heappop(rhp)
            heapq.heappush(lhp, -right)
            heapq.heappush(rhp, left)
    print(-lhp[0])