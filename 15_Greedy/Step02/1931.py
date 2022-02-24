#BOJ 1931
import sys

num = int(input())

room = []
for i in range(num):
    room.append(list(map(int, sys.stdin.readline().split())))

room.sort(key = lambda x:(x[1], x[0]))

cnt = 0
for i in range(num):
    if i == 0:
        cnt += 1
        end_time = room[i][1]
    else:
        if room[i][0] >= end_time:
            cnt += 1
            end_time = room[i][1]
        else:
            continue
print(cnt)