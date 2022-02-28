#BOJ 18258
#2028ms. 이것보다 적게 걸린 풀이는 다를 게 없지만 cmd 리스트가 아닌 문자열로 처리한다는 차이가 있음(1536ms)
import sys
from collections import deque
input = sys.stdin.readline
dq = deque()

num = int(input())
for i in range(num):
    cmd = list(input().split())
    if cmd[0] == 'push':
        dq.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    else:
        if not dq:
            print(-1)
        else:
            print(dq[-1])