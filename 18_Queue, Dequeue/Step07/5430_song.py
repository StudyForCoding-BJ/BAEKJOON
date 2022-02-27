# BOJ 5430
# 300ms
# 40164KB

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for i in range(N):
    oper = input()
    n = int(input())
    
    user_input  = input()
    
    if n != 0:
        arr_string = user_input[1:len(user_input)-2]
        arr = list(map(int, arr_string.split(',')))
    else:
        arr = []

    queue = deque(arr)
    
    err = 0
    rcount = 0
    for i in oper:
        
        if i == 'R':
            rcount += 1

        elif i == 'D':
            
            if queue:
                if rcount % 2 != 0: # 홀수면
                    queue.pop()
                else:               # 짝수면
                    queue.popleft() 
            
            else:
                print('error')
                err += 1
                break
            
    if err == 0:
        if rcount % 2 != 0:
            queue.reverse()
            result = ','.join(map(str, queue))
        else:
            result = ','.join(map(str, queue))
        print(f'[{result}]')