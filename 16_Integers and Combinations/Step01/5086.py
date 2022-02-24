#BOJ 5086
import sys
def sol(a:list):
    f, s = a[0], a[1]
    if f == 0 and s == 0:
        exit()
    if s%f == 0:
        return ("factor")
    elif f%s == 0:
        return ("multiple")
    else:
        return("neither")
while True:
    print(sol(list(map(int, sys.stdin.readline().split()))))