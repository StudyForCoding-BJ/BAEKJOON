#BOJ 2580
#다른 풀이 참조
#python3는 4613ms, 30864KB
#pypy3는 1040ms, 136104KB
import sys
board = [[0]*9 for i in range(9)]
row = [[False]*10 for i in range(9)]
col = [[False]*10 for i in range(9)]
sqr = [[False]*10 for i in range(9)]

for i in range(9):
    n = 0
    for k in list(map(int, sys.stdin.readline().split())):
        board[i][n] = k
        n += 1
    for j in range(9):
        if board[i][j] != 0:
            row[i][board[i][j]] = True
            col[j][board[i][j]] = True
            sqr[(i//3)*3+(j//3)][board[i][j]] = True
def sol(a: int):
    x = a//9
    y = a%9
    
    if a == 81:
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit()
    if board[x][y] == 0:
        for i in range(1, 10):
            if row[x][i] == False and col[y][i] == False and sqr[(x//3)*3+(y//3)][i] == False:
                row[x][i] = True
                col[y][i] = True
                sqr[(x//3)*3+(y//3)][i] = True
                board[x][y] = i
                sol(a+1)
                board[x][y] = 0
                row[x][i] = False
                col[y][i] = False
                sqr[(x//3)*3+(y//3)][i] = False
    else:
        sol(a+1)
sol(0)