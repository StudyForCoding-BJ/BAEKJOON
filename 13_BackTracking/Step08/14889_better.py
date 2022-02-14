#BOJ 14889 _ better
#pypy3 436ms, python3 2704ms
import sys

num = int(input())
board = [list(map(int, sys.stdin.readline().split())) for i in range(num)]

start = [0]
mini = []

def sol():
    if len(start) == num//2:
        link=[]
        for i in range(num):
            if i not in start:
                link.append(i)
        st, li = 0, 0
        for i in range(num//2):
            for j in range(num//2):
                st += board[start[i]][start[j]]
                li += board[link[i]][link[j]]
        mini.append(abs(st-li))
    for i in range(start[-1]+1, num):
        start.append(i)
        sol()
        start.pop()
sol()
print(min(mini))