#BOJ 2108 _ lib
#325B, 620ms

import sys
import statistics

num = int(input())
numlist = [int(sys.stdin.readline()) for i in range(num)]
numlist.sort()
print(round(statistics.fmean(numlist)))
print(statistics.median(numlist))
mode = statistics.multimode(numlist)
if len(mode) != 1:
    print(mode[1])
else:
    print(mode[0])
print(numlist[-1]-numlist[0])