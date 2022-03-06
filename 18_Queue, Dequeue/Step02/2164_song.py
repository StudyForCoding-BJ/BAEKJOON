# BOJ 2164
# 440ms
# 50292KB
# 원형큐로 구현

N = int(input())
queue = [i for i in range(1, N+1)]
front = 0
rear = 0
queue_size = N

def card():
    
    global front, rear, queue_size
      
    # 제일 위에 있는 카드 버림
    queue[front] = 0
    front += 1
    queue_size -= 1
    
    if front == N:
        front = 0
    
    # 제일 위에 있는 카드 맨 밑으로 옮김
    queue[rear] = queue[front]
    queue[front] = 0
    front += 1
    rear += 1
    if rear == N:
        rear = 0
    if front == N:
        front = 0
    
while queue_size != 1:
    card()

print(max(queue))
    