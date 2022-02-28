#BOJ 10866
#Python deque 자체가 시간이 오래걸리는 자료구조인듯. List로 구현한 deque가 훨씬 시간이 빠름(80ms)
import sys
from collections import deque
input = sys.stdin.readline
num = int(input())
dq = deque()

for i in range(num):
    cmd = list(input().split())
    if cmd[0] == 'push_front':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        dq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)