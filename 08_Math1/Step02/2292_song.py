N = int(input())

num = 1 #벌집개수
i = 1 

while N > num :
    
    num += 6 * i
    i += 1
    
print(i)
