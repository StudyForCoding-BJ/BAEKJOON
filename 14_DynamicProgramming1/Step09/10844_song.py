N = int(input())


arr = [[0]*10 for _ in range(N)]
arr[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        if j == 0:
            arr[i][0] = arr[i-1][1]
        elif j == 9:
            arr[i][9] = arr[i-1][8]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
            
print(sum(arr[N-1])%1000000000)
        
    