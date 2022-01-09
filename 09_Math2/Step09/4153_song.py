while 1:
    data = [int(x) for x in input().split()]
    
    if(data[0] == 0):
        break
    
    bit = max(data)
    data.remove(bit)
    
    if(bit**2 == data[0]**2 + data[1]**2):
        print('right')
        
    else:
        print('wrong')
