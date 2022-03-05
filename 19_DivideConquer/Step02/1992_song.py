# BOJ 1992
# 72ms
# 30864KB
import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip() for _ in range(N)) # 문자열로 받음

result = ''
def quadtree(n, row, col):
    
    global result
    
    if n == 1: # 한 칸 일 때
        if arr[row][col] == '1':
            result += '1'
            return
        else:
            result += '0'
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
        if check == '1':
            result += '1'
            return
        else:
            result += '0'
            return
    
    else: # 다 안같으면 분할     
        n = n // 2
        col_mid = col + n
        row_mid = row + n
        
        result += '('
        
        # 행, 렬
        quadtree(n, row, col) 
        quadtree(n, row, col_mid) 
        quadtree(n, row_mid, col) 
        quadtree(n, row_mid, col_mid)
        
        result += ')'
        
quadtree(N, 0, 0)
print(result)