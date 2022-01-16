import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    d = int(sys.stdin.readline().strip())
    data.append(d)

n = len(data)
for i in range(0 , n-1):
    exchange = 0
    
    for j in range(n-1, i, -1):
        
        if data[j-1] > data[j]:
            data[j-1], data[j] = data[j], data[j-1]
            exchange += 1
            
    if exchange == 0:
        break

for i in data:
    print(i)

