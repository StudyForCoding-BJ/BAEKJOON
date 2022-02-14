import sys

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(N-1, 0, -1):
    for j in range(i):
        arr[i-1][j] = arr[i-1][j] + max(arr[i][j], arr[i][j+1])
        
print(arr[0][0])
