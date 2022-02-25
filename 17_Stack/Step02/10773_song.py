# BOJ 10773 
# 108ms
# 31640KB

# input 뺐을 때 8ms 시간 감소

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))