n = int(input())
L = list()

if n < 100:
    
    count = n

else:

    count = 99
    
    for i in range (100, n+1):
            
        L.clear()
        s = str(i)
            
        for a in s:
                
            L.append(int(a))

        if(L[2]-L[1] == L[1]-L[0]):
            count += 1
            
print(count)

                
        
        
        
