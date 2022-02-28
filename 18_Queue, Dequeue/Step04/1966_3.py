#BOJ 1966 _ 3
#92ms
#idx를 deque가 아닌 list로 바꿔 봄
#차이 없음
from collections import deque
import sys
tc = int(input())
for i in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    p = deque(map(int, sys.stdin.readline().split()))
    idx = list(range(n))
    
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
                del idx[0]
        else:
            p.append(p.popleft())
            idx.append(idx[0])
            del idx[0]