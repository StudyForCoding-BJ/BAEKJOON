#BOJ 9663
#pypy3

num = int(input())
board = [0]*(num+1)
cnt = 0
visited = [False]*(num+1)

def sol(a: int):
    if a == num:
        global cnt
        cnt += 1
    else:
        for i in range(num):
            if visited[i]:
                continue
            board[a] = i
            if queen(a) == True:
                visited[i] = True
                sol(a+1)
                visited[i] = False
def queen(a: int):
    for i in range(a):
        if board[a] == board[i] or a - i == abs(board[a]-board[i]):
            return False
    return True

sol(0)
print(cnt)