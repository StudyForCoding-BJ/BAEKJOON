# 15%에서 시간초과

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
findmem = list(map(int, input().split()))

arr.sort()


def numcard(arr, start, end):
    
    global count
    
    if start > end:
        return 
    
    mid = (start + end) // 2
    if arr[mid] == num:
        
        return count
        
    elif arr[mid] > num:
        return numcard(arr, start, mid - 1)
            
    else:
        return numcard(arr, mid + 1, end)

result = []
for i in findmem:
    count = 0
    num = i
    numcard(arr, 0, N-1)   
    result.append(count)    
print(*result) 

