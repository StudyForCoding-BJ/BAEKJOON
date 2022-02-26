# BOJ 1874
# 268ms
# 36304KB

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

stack = [0]
result = []
count = 0           
for i in arr:
    for j in range(count+1, N+2):
        
        if i >= j: # 원하는 수가 나오면 일단 push
            stack.append(j)
            result.append('+')
            
        elif i == stack[-1]: # 원하는 수가 stack에 있으면 pop
            if count < stack[-1]:
                count = stack[-1]
            stack.pop()
            result.append('-')
            break
        
        else:
            print('NO')
            exit(0)
        
for i in result:
    print(i)    
            
    