# BOJ 4949
# 100ms
# 30860KB

import sys
input = sys.stdin.readline

table = {
    ')' : '(',
    ']' : '[',
}

def balance(string):
    for i in string:
        # ( 이나 [ 일 경우 push
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')' or i == ']':
            # 스택이 비어있거나 스택 마지막 요소와 짝이 안맞을 경우
            if len(stack) == 0 or table[i] != stack[-1]: 
                print('no')
                return
            # 짝이 맞으면 pop
            else:
                stack.pop()
                
    # string 다 돌았는데 stack이 남아있는 경우             
    if len(stack) != 0:
        print('no')
        return
    else:
        print('yes')
        return
             
while True:
    stack = []
    string = input()
    
    if string == ".\n":
        break
    
    balance(string)

# 문자열을 append해서 시간이 좀 더 걸린 것 같음
