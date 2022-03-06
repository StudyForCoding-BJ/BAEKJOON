# BOJ 18258
# 1984ms
# 143764KB

import sys
input = sys.stdin.readline

N = int(input())

queue = [None] * N
front  = 0
rear = 0
queue_size = 0

for i in range(N):
    user_input = input().split()
    com = user_input[0]
    
    if com == 'push':
        value = user_input[1]
        queue[rear] = value
        rear += 1
        queue_size += 1
        
    elif com == 'pop':
        if queue_size == 0:
            print(-1)
        else:
            print(queue[front])
            queue[front] = None
            front += 1
            queue_size -= 1
            
    elif com == 'size':
        print(queue_size)
    
    elif com == 'empty':
        if queue_size == 0:
            print(1)
        else:
            print(0)
            
    elif com == 'front':
        if queue_size == 0:
            print(-1)
        else:
            print(queue[front])
            
    elif com == 'back':
        if queue_size == 0:
            print(-1)
        else:
            print(queue[rear-1])
