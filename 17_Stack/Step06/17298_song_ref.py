# BOJ 17298
# 1072ms
# 197240KB
# 시간은 단축되지만 메모리를 더 씀

n = int(input())
answer = [-1] * n
numbers=list(map(int,input().split()))
stack=[]

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i] :
        answer[stack.pop()]=numbers[i]
    stack.append(i)

print(" ".join(map(str,answer)))
