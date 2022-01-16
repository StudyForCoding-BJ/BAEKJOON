import sys

N = int(input())

arr = []
for i in range(N):
    arr.append(sys.stdin.readline().strip())

arr2 = []
for j in arr:
    if j not in arr2:
        arr2.append(j)

arr2.sort()
arr2.sort(key=len)

for i in arr2:
    print(i)
    
