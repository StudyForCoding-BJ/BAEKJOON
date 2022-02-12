import sys
N = int(input())

wine = [0] * 10001
for i in range(1, N + 1):
    wine[i] = int(sys.stdin.readline())

arr = [0] * 10001
arr[1] = wine[1]
arr[2] = wine[1] + wine[2]

for i in range(3, N + 1):
    arr[i] = max(arr[i-3] + wine[i-1] + wine[i], arr[i-2] + wine[i], arr[i-1])

print(arr[N])
    