import sys

N = int(input())
data = [int(sys.stdin.readline()) for i in range(N)]

def fibo(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1

    global arr1
    
    for i in range(2, n+1):
        num = arr1[i-2] + arr1[i-1]
        arr1.append(num)

    return arr1[n]

for i in data:
    arr0 = [1]
    arr1 = [0, 1]
    fibo(i)
    arr0 += arr1
    print(arr0[i], arr1[i])
    
