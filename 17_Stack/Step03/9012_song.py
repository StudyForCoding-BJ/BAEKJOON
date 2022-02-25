# 68ms
# 30864KB

import sys
input = sys.stdin.readline

N = int(input())

def find_VPS():
    string = input()
    stack = []
    for k in string:
        if k == '(':
            stack.append(k) 
        elif k == ')':
            if len(stack) == 0: # stack이 비었을 경우
                print('NO')
                return
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
        return
    else:
        print('YES')
        return

for i in range(N):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    find_VPS()
                