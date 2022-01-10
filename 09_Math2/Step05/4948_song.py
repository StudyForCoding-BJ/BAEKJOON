def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

#시간초과 해결
a=[]
for i in range(2, 246913):
    if(is_prime(i)):
        a.append(i)

while 1:
    count = 0
    temp = int(input())
    
    if temp == 0:
        break

    for k in a:
        if(temp < k <= 2*temp):
            count += 1
            
    print(count)


 

    
    
