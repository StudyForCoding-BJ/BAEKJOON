#BOJ 2108
#520B, 540ms
#최빈값 다른 풀이 참조
#이것보다 시간 단축하는 풀이: 아예 처음부터 0~8000 배열 만들어서 카운팅 소트 구현

import sys

num = int(input())
numlist = [int(sys.stdin.readline()) for i in range(num)]
numlist.sort()

print(round(sum(numlist)/num))
print(numlist[num//2])

rec = -4001
cnt = 0
update = 1
cntlist = []
for i in numlist:
    if i == rec:
        cnt += 1
    else:
        cnt = 1
    
    if cnt == update:
        cntlist.append(i)
    elif cnt > update:
        cntlist = [i]
        update = cnt
    rec = i

if len(cntlist) != 1:
    print(cntlist[1])
else:
    print(cntlist[0])


print(numlist[num-1]-numlist[0])