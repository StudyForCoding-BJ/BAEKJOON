import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

result = []
arr_max = max(arr)


for i in range(2, arr_max+1):
    temp = arr[0] % i
    count = 1
    for m in arr:
        if m % i == temp:
            count += 1
    if count == len(arr)+1:
        result.append(i)   

print(*result)