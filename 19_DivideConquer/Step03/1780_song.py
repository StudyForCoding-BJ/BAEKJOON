# BOJ 1780
# 3376ms
# 68784KB

import sys
input = sys.stdin.readline

N = int(input())
arr  = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
one = 0

def whatis(check):
    
    global minus, zero, one
    
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        one += 1

def paper(n, row, col):
    check = arr[row][col]
    
    if n == 1:
        whatis(check)
        return

    count = 0
    for i in range(row, row + n):
        for j in range(col, col + n):
            if arr[i][j] != check:
                count += 1
                break
        if count != 0:
            break
    
    if count == 0: # 같으면 종이로 사용
        whatis(check)
    else: # 안같으면 분할
        n = n // 3
        row1 = row + n
        row2 = row1 + n
        col1 = col + n
        col2 = col1 + n
        
        paper(n, row, col)
        paper(n, row, col1)
        paper(n, row, col2)
        paper(n, row1, col)
        paper(n, row1, col1)
        paper(n, row1, col2)
        paper(n, row2, col)
        paper(n, row2, col1)
        paper(n, row2, col2)

paper(N, 0, 0)
print(minus)
print(zero)
print(one)
    