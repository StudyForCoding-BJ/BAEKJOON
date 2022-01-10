N = int(input())

for i in range(N):
    k = int(input())
    n = int(input())

    #초기화
    arr = [[0]*n]*(k+1)
    
    for j in range(k+1):
        arr[j][0] = 1
    for i in range(1, n+1):
        arr[0][i-1] = i
    

    for a in range(1, k+1):
        for b in range(1, n):
            arr[a][b] = arr[a][b-1] + arr[a-1][b]
    print(arr[k-1][n-1])
