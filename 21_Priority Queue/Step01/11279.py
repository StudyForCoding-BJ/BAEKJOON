#BOJ 11729
#priority queue 이용
#38848KB, 384ms
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
q = PriorityQueue(n)

for i in range(n):
    x = int(input())
    if x == 0:
        if not q.empty():
            print(-q.get())
        else:
            print(0)
    else:
        q.put(-x)