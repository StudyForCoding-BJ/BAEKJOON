#10184ms

N = int(input())

result = 0
column = []
d_right = []
d_left = []

def queen(x): 
    
    global result
    
    if x == N + 1:
        result += 1
        return
    
    for y in range(1, N + 1):
        if y not in column: # column check
            if (x - y) not in d_right: # right diagonal check
                if (x + y) not in d_left: # left diagonal check
                    # (x, y) 를 Q로 지정
                    column.append(y)
                    d_right.append(x - y)
                    d_left.append(x + y)
                    queen(x + 1)
                    column.pop()
                    d_right.pop()
                    d_left.pop()
          
queen(1)  

print(result)