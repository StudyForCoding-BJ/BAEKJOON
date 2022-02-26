# BOJ 2164
# 244ms
# 53324KB
# 덱으로 구현
import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N+1)])
    
def card():
    while queue:
        # 제일 위에 있는 카드 버림
        tmp = queue.popleft()
        if len(queue) == 0:
            print(tmp)
            break
        #  제일 위에 있는 카드 맨 밑으로 옮김
        queue.append(queue.popleft())
    
card() 