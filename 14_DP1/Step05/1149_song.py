import sys
N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(N-1, 0, -1):
    #0 -> 1, 2 (빨간색으로 칠하는 경우)
    arr[i-1][0] = arr[i-1][0] + min(arr[i][1], arr[i][2])
    #1 -> 0, 2 (초록색으로 칠하는 경우)
    arr[i-1][1] = arr[i-1][1] + min(arr[i][0], arr[i][2])
    #2 -> 0, 1 (파란색으로 칠하는 경우)
    arr[i-1][2] = arr[i-1][2] + min(arr[i][0], arr[i][1])
    
print(min(arr[0]))