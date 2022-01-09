N = int(input())

a = list(map(int, input().split()))
cnt = len(a)

for i in a:
    
    if(i == 1):
        cnt -= 1
    
    elif(i == 2):
        pass
        
    else:
        for j in range(2, i):
            if(i%j == 0):
                cnt -= 1
                break

print(cnt)

    
