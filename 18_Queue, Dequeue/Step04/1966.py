#BOJ 1966
#100ms(96ms)
#Index를 list 없이 연산으로
from collections import deque
import sys
tc = int(input())
for i in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    p = deque(map(int, sys.stdin.readline().split()))
    
    t = p[m]
    cnt = 0
    
    while True:
        if p[0] == max(p):
            cnt += 1
            if p[0] == t:
                if m == 0:
                    print(cnt)
                    break
                else:
                    p.popleft()
                    m -= 1
            else:
                p.popleft()
                m -= 1
        else:
            p.append(p.popleft())
            m = (m-1+len(p))%len(p)