#BOJ 1149
#다른 풀이 참조
#72ms, 571BB
import sys
sys.setrecursionlimit(10**9)

num = int(input())
max_cost = 3001

table = []
for i in range(num):
    table.append(list(map(int, sys.stdin.readline().split())))

memo = [[3001]*3 for i in range(num)]

def paint(a, b):
    if a == num-1:
        return table[a][b]
    if memo[a][b] != 3001:
        return memo[a][b]
    
    cand = []
    for i in range(3):
        if i == b:
            continue
        else:
            cand.append(paint(a+1, i)+table[a][b])
    memo[a][b] = min(cand)
    return memo[a][b]

print(min(paint(0,0), paint(0,1), paint(0,2)))