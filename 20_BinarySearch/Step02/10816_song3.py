# 30%에서 시간초과
# pypy 73%에서 초과

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
findmem = list(map(int, input().split()))

arr.sort()

def numcard(arr, num, start, end):
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            temp = mid - 1
            temp2 = mid + 1
            while temp >= 0 and arr[temp] == num: # 왼쪽 탐색
                temp -= 1
            
            while temp2 < N and arr[temp2] == num: # 오른쪽 탐색
                temp2 += 1
                
            count = temp2 - temp - 1
            return count
        
        elif arr[mid] < num: # 오른쪽 탐색
            start = mid + 1
        else: # 왼쪽 탐색
            end = mid -1 
    return count

result = []
for i in findmem:
    result.append(numcard(arr, i, 0, N-1))    
print(*result) 