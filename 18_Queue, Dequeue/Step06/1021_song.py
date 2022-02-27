# BOJ 1021
# 88ms
# 32404KB

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
loc = list(map(int, input().split()))

queue = deque([i for i in range(1, N+1)])

count = 0
for i in loc:
    location = queue.index(i)
    
    while i != queue[0]:
        
        if len(queue) % 2 == 0:
            # 꺼내야 할 수의 인덱스가 총 덱 길이의 반보다 클 경우 ->  rotate(1)
            if location >= len(queue) // 2:
                queue.rotate(1)
                location += 1
                count += 1
            
                if location == len(queue):
                    location = 0
            # 꺼내야 할 수의 인덱스가 총 덱 길이의 반보다 작을 경우 ->  rotate(-1)
            else:
                queue.rotate(-1)
                location -= 1
                count += 1
                
                if location == -1:
                    location = len(queue)
                    
        elif len(queue) % 2 != 0:
            if location > len(queue) // 2:
                queue.rotate(1)
                location += 1
                count += 1
            
                if location == len(queue):
                    location = 0
            else:
                queue.rotate(-1)
                location -= 1
                count += 1
                
                if location == -1:
                    location = len(queue)
    
    queue.popleft()
print(count)
    