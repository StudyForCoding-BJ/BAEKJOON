# BOJ 11866
# 92ms
# 32344KB

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
result = []
idx = 0

while len(queue) != 1:
    
    idx += K - 1
    
    # 원형큐
    while idx > len(queue)-1:
        idx = idx - len(queue)
    
    result.append(queue[idx])
    del queue[idx]
result.append(queue[0])

string = ', '.join(map(str, result))
print(f'<{string}>')
    
 