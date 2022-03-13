# BOJ 10816
# 1144ms
# 114524KB

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
findmem = list(map(int, input().split()))

arr.sort()
duplicate = {}
for n in arr:
    if n not in duplicate:
        duplicate[n] = 1
    else:
        duplicate[n] += 1

for i in findmem:
    if i in duplicate:
        print(duplicate[i], end=" ")
    else:
        print(0, end=" ")
   
