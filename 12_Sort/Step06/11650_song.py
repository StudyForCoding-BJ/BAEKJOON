import sys
N = int(input())

arr = []
for i in range(N):
    (x, y) = map(int, sys.stdin.readline().split())
    arr.append((x, y))
    
arr = sorted(arr, key=lambda a: (a[0], a[1]))
#arr = sorted(arr) <- 이렇게 해도 

for i in range(N):
    print(arr[i][0], arr[i][1])



