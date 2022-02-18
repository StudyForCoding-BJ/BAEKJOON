#combination이용
#PyPy3 732ms
#192240KB

import sys, itertools
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
decision = [i for i in range(N)]

#팀 나누기
nCr = list(itertools.combinations(decision, N//2))
start= []
for i in nCr:
    start.append(list(i))
    
output = []
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
    
#filtering                    
for i in start:   
    calcul_ability(i)

print(min(output))     
                                                                                                      