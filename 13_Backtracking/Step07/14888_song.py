#120ms

import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))

def oper_decision(i, n, temp):
    if i == 0:
        return temp + arr[n+1]
    elif i == 1:
        return temp - arr[n+1]
    elif i == 2:
        return temp * arr[n+1]
    else:
        if temp < 0:
            temp2 = temp * (-1) // arr[n+1] * (-1)
        else:
            temp2 = temp // arr[n+1]
        return temp2

output = []
def oper_inter(n, temp_cur):
    # exit condition
    if n == N-1:
        output.append(temp_cur)
        return
    
    # filtering
    for i in range(4):
        if oper[i] != 0:
            
            # calculate, use oper
            temp = oper_decision(i, n, temp_cur) 
            oper[i] -= 1
            
            # recursion
            oper_inter(n+1, temp)
            
            # return 시 되돌리기
            temp = temp_cur
            oper[i] += 1
            

temp = arr[0]
oper_inter(0, temp)
print(max(output))
print(min(output))
