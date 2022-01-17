#BOJ 7568
# k+= 1을 아예 밖으로 뺄 때와 if, else 처리를 할 때 -> if, else 처리 할 때가 4ms 덜 나오는데 왜 그럴까
import sys

num = int(input())
info = []
for i in range(num):
    info.append(list(map(int, sys.stdin.readline().split())))

sorted_weight = sorted(info)

for i in info:
    j = sorted_weight.index(i)
    k = j
    score = 1
    while k < num:
        if sorted_weight[j][1] < sorted_weight[k][1]:
            if sorted_weight[j][0] != sorted_weight[k][0]:
                score += 1
                k += 1
            else:
                k += 1
    print(score, end=' ')
