# 312ms
# 51636KB

import sys
N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0]) # 시작하는 시간
arr.sort(key=lambda x:x[1]) # 끝나는 시간 


count = []
count.append(arr[0])
for i in range(1, N):
    pre_end = count[-1][1] # 마지막으로 선택된 회의 끝 시간
    start = arr[i][0] # 회의 시작 시간
    if start >= pre_end:
        count.append(arr[i])

print(len(count))

'''
시작하는 시간 순으로 정렬하는 이유? 
-> [3, 3], [2, 3], [3, 3]의 경우 이렇게 끝나는 시간이 정렬되면
[2, 3] 회의는 할 수 없다고 판단, 최대 2개가 답이됨
but 실제로는 [2, 3], [3, 3], [3, 3] 순이면 3개의 회의를 모두 할 수 있음
'''