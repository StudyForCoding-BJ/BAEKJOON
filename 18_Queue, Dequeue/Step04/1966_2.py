#BOJ 1966 _ 2
#92ms
#Index를 deque화
from collections import deque
import sys
tc = int(input())
for i in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    p = deque(map(int, sys.stdin.readline().split()))
    idx = deque(range(n))
    
    t = idx[m]
    cnt = 0
    
    while True:
        if p[0] == max(p):
            cnt += 1
            if idx[0] == t:
                print(cnt)
                break
            else:
                p.popleft()
                idx.popleft()
        else:
            p.append(p.popleft())
            idx.append(idx.popleft())