N = int(input())


for i in range(N):
    x, y= map(int, input().split())
    
    count = 0
    move = 1
    distance = y - x
    cur = 0

    while cur < distance:
        
        cur += move
        count += 1
        
        if count % 2 == 0:
            move += 1

    print(count)
        

    
