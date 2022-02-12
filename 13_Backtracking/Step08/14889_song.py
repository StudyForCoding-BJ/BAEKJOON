#시간초과

import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
decision = [i for i in range(N)]


def calcul_ability(start):
    
    #start팀 능력치
    result_start = 0
    for i in start:
        for j in start:
            if i != j:
                result_start += arr[i][j]       
            
    #link팀 능력치
    link = []
    for k in decision:
        if k not in start:
            link.append(k)
    result_link = 0
    for i in link:
        for j in link:
            if i != j:
                result_link += arr[i][j]
                
    output.append(abs(result_start-result_link))
    

start = []
output = []
def start_link(depth):
    #exit condition
    if len(start) == N // 2:
        calcul_ability(start)
        return                                                 
                  
    #filtering                    
    for i in range(N):
        if i not in start:
            start.append(i)
            #recursion    
            depth += 1
            start_link(depth)
            #return 후 되돌리기
            depth -= 1
            start.pop()

start_link(0)
print(min(output))     
                                                                                                      