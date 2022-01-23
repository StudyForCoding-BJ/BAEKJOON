#BOJ 1984
#더 빠른 풀이로는 2차원 배열 생성 후 같은 메모이제이션 하는 풀이가 있었음.
#메모리를 늘리고 시간을 줄이느냐 메모리를 줄이고 시간을 늘리느냐의 차이로 보임.
import sys

rec = {}

def w(a: list):
    if a[0] <= 0 or a[1] <= 0 or a[2] <= 0:
        return 1
    elif a[0] > 20 or a[1] > 20 or a[2] > 20:
        return w([20, 20, 20])
    if rec.get(tuple(a)) != None:
        return rec.get(tuple(a))
    else:
        if a[0]<a[1] and a[1]<a[2]:
            rec[tuple(a)] = w([a[0], a[1], a[2]-1]) + w([a[0], a[1]-1, a[2]-1]) - w([a[0], a[1]-1, a[2]])
        else:
            rec[tuple(a)] = w([a[0]-1, a[1], a[2]]) + w([a[0]-1, a[1]-1, a[2]]) + w([a[0]-1, a[1], a[2]-1]) - w([a[0]-1, a[1]-1, a[2]-1])
        return rec.get(tuple(a))

while True:
    case = list(map(int, sys.stdin.readline().split()))
    if case == [-1, -1, -1]:
        exit()
    else:
        res = w(case)
        print(f'w{tuple(case)} = {res}')