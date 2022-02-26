# BOJ 18258
# 1536ms
# 141632KB
# deque 이용


from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
queue=deque()
for i in range(n):
    command=input().rstrip()
    if 'push' in command:
        queue.append(command.split()[1])
    elif 'pop' in command:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if queue:
            print(queue[-1])
        else:
            print(-1)