# BOJ 2630
# 76ms
# 30864KB

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

# n, 시작 row, 시작 col    
def confetti(n, row, col):
    
    global white, blue
    
    if n == 1: # 한 칸 일 때
        if arr[row][col] == 1:
            blue += 1 
            return
        else:
            white += 1
            return 
        
    count = 0
    # 범위 내 모든 값이 동일한지 확인
    check = arr[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if arr[i][j] != check: 
                count += 1 
                break
        if count != 0:
            break
    
    if count == 0: # 다 같으면              
        if check == 1:
            blue += 1
        else:
            white += 1
        return
    
    else: # 다 안같으면 분할     
        n = n // 2
        col_mid = col + n
        row_mid = row + n
        
        # 행, 렬
        confetti(n, row, col) # 0, 0 ~ 3, 3 # 0, 0
        confetti(n, row, col_mid) # 0, 4 ~ 3, 7 # 0, 4
        confetti(n, row_mid, col) # 4, 0 ~ 7, 3 # 4, 0
        confetti(n, row_mid, col_mid) # 4, 4 ~ 7, 7 # 4, 4
        
confetti(N, 0, 0)
print(white)
print(blue)

