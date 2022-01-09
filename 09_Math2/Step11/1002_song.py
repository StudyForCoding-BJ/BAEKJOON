import math
N = int(input())

result = []
for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
    rplus = r1 + r2
    rminus = abs(r1-r2)
    
    if distance == 0:
        
        if(r1 != r2):
            result.append(0)
        else:
            result.append(-1)
            
    elif rminus < distance < rplus:
        result.append(2)
    elif rplus == distance or rminus == distance:
        result.append(1)
    else:
        result.append(0)

for j in result:
    print(j)
    

