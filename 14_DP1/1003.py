#BOJ 1003
import sys

test = int(input())

def fibonacci(a: int, memo: list):
    if a == 0:
        memo.append([1, 0])
    elif a == 1:
        memo.append([1, 0])
        memo.append([0, 1])
    else:
        tmp = fibonacci(a-1, memo)
        memo.append([tmp[-1][0]+tmp[-2][0], tmp[-1][1]+tmp[-2][1]])
    return memo

for i in range(test):
    print(' '.join(map(str, fibonacci(int(sys.stdin.readline()), [])[-1])))