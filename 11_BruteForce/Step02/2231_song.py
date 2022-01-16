N = int(input())

def B(n):
    
    if(n == 1):
        print(0)
        
    else:
        for i in range(1, n):
            temp = i
            result = i
            
            #분해합
            while temp != 0:
                result += temp % 10
                temp = temp // 10

            if result == n:
                print(i)
                break
        
            elif i == n-1:
                print(0)
        
B(N)


    
    
    
