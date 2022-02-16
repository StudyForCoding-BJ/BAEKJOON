#시간초과

import sys
N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])
# print(arr)

room_arr = [-1]
count = [0] * 1000001

def room(meeting):
    start = meeting[0]
    end = meeting[1]
    for i in range(len(room_arr)):
        #방 없으면 방 만들기
        if i == (len(room_arr)-1):
            room_arr.append(end)
            count[i+1] += 1
            
        if room_arr[i] <= start: #전 회의 끝나는 시간이 회의 시작시간보다 작을 경우
            room_arr[i] = end
            count[i] += 1
        #아니면 다음 방 탐색
            
for i in arr:
    room(i)

# print(room_arr)
print(max(count))
