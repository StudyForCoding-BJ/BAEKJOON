#BOJ 1927 _ 2
#Priority Queue
#38848KB, 372ms
#heapq와 PQ의 메모리 차이는 없다고 봐야
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
q = PriorityQueue(n)

for i in range(n):
    x = int(input())
    if x == 0:
        if not q.empty():
            print(q.get())
        else:
            print(0)
    else:
        q.put(x)