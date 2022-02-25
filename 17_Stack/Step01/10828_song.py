# BOJ 10828
# 76ms
# 30864KB

import sys

N = int(input())

stack = []

for i in range(N):
    user_input = sys.stdin.readline().split()
    com = user_input[0]
    
    if com == 'push':
        value = int(user_input[1])
        stack.append(value)
        
    elif com == 'pop':
        if len(stack) != 0:
            a = stack.pop()
            print(a)
        else:
            print(-1)
            
    elif com == 'size':
        print(len(stack))
    
    elif com == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif com == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    
    

    
    

















for i in range(N):
    user_input = sys.stdin.readline().split()
    if user_input[0] == 'push':
        value = int(user_input[1])
        
    print(user_input)
    

# def select_oper() -> Oper:
#     n = input()
#     return 
