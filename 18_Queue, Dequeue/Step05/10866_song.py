# BOJ 10866
# 104ms
# 32404KB

from collections import deque
import sys
input = sys.stdin.readline
 
N = int(input())

queue = deque()
for i in range(N):
    user_input = input().split()
    com = user_input[0]
    
    if com == 'push_front':
        value = int(user_input[1])
        queue.appendleft(value)
        
    elif com == 'push_back':
        value = int(user_input[1])
        queue.append(value)
        
    elif com == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
            
    elif com == 'size':
        print(len(queue))
    elif com == 'empty':
        if queue:
            print(0)
        else:
            print(1)
            
    elif com == 'front':
        if len(queue) == 0:
                print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
                print(-1)
        else:
            print(queue[-1])