#BOJ 14889
#pypy3 1176ms
import sys
num = int(input())
ppl = [0]*20
board = []
mini = 100000
for i in range(num):
    board.append(list(map(int, sys.stdin.readline().split())))

def sol(cnt: int, idx: int):
    global mini
    
    if cnt == num//2:
        start = 0
        link = 0
        for i in range(num):
            for j in range(num):
                if ppl[i] == 1 and ppl[j] == 1:
                    start += board[i][j]
                if ppl[i] == 0 and ppl[j] == 0:
                    link += board[i][j]
        tmp = abs(start-link)
        if mini > tmp:
            mini = tmp
            
        return
    
    for n in range(idx, num):
        ppl[n] = 1
        sol(cnt+1, n+1)
        ppl[n] = 0
sol(0, 0)
print(mini)