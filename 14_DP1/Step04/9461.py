#BOJ 9461
import sys

num = int(input())
memo = [0] * 101

def seq(a: int):
    if a == 0:
        return 0
    if a == 1 or a == 2:
        return 1
    if memo[a] != 0:
        return memo[a]
    else:
        memo[a] = seq(a-2) + seq(a-3)
        return memo[a]

for i in range(num):
    print(seq(int(sys.stdin.readline())))