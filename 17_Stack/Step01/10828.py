#BOJ 10828
#일일이 함수로 만들어 구현했을 때(84ms)에 비해 80ms로 전혀 차이를 보이지 않음.
#2차 수정: pop(-1)로 구현하다가 pop()으로 바꿔 봤는데 큰 차이는 없음.
#애초에 -1을 넣으면 pop()이랑 똑같은 거니까 상관은 없겠지만 만약에 pop(len(arr)-1)로 한다면 시간이 오래 걸릴 수도 있을 것
import sys
input = sys.stdin.readline

num = int(input())

stack = [] 

for i in range(num):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)