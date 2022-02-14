import sys

N = int(input())

data = list(int(input()) for _ in range(N))

def pado(n):
    arr = [0, 1, 1, 1, 2, 2, 3]
    
    for i in range(7, n+1):
        arr.append(arr[i-1] + arr[i-5])
        
    return arr[n]

for i in data:
    result = pado(i)
    print(result)
    
