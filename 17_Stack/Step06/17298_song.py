# BOJ 17298
# 1388ms
# 151420KB

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = [arr[N-1]]
result = [-1] # 마지막 숫자는 항상 비교할 수가 없음
for i in range(N-2, -1, -1):
    
    if arr[i] >= stack[-1]: # 현재수가 더 크거나 같을 경우
        stack.pop()
        while len(stack) != 0:
            if arr[i] < stack[-1]:
                result.append(stack[-1])
                stack.append(arr[i])
                break
            stack.pop()
        
        if len(stack) == 0: # stack 비었을 경우
            result.append(-1)
            stack.append(arr[i])
            
    else: # 현재수가 작을 경우
        result.append(stack[-1])
        stack.append(arr[i])   

print(*result[::-1])