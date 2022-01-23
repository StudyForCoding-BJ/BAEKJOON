#BOJ 1932
#160ms
import sys

size = int(input())

table = []
for i in range(size):
    table.append(list(map(int, sys.stdin.readline().split())))
    
memo = [[None]*len(i) for i in table]

memo[0][0] = table[0][0]

for i in range(1,size):
    memo[i][0] = memo[i-1][0] + table[i][0]
    memo[i][-1] = memo[i-1][-1] + table[i][-1]
    for j in range(1, i):
        memo[i][j] = max(memo[i-1][j-1], memo[i-1][j]) + table[i][j]

print(max(memo[-1]))