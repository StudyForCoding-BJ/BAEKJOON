#BOJ 2108 _ better
#706B, 372ms

import sys

num = int(input())
arr = [0]*8001

updateMax = -4000
updateMin = 4000

sumNm = 0
for i in range(num):
    val = int(sys.stdin.readline())
    sumNm += val    #미리 합 계산
    arr[4000+val] += 1
    
    if val>updateMax:
        updateMax = val
    if val<updateMin:
        updateMin = val

cnt = 0
for i in range(8001):
    cnt += arr[i]
    if cnt >= num/2:
        mid = i-4000
        break

maxCnt = max(arr)
if arr.count(maxCnt) != 1:
    modelist = []
    for i in range(8001):
        if arr[i] == maxCnt:
            modelist.append(i-4000)
    mode = modelist[1]
else:
    mode = arr.index(maxCnt)-4000

print(round(sumNm/num))
print(mid)
print(mode)
print(updateMax-updateMin)