# import time
# start_time = time.process_time()
import sys

sdoku = []
for i in range(9):
    temp = list(map(int, sys.stdin.readline().split()))
    sdoku.append(temp)

bin = []
#빈칸 미리 찾아놓기
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            temp = [i, j]
            bin.append(temp)  
bin.append([-1, -1])

output = []           
def sdoku_f(x, y, num, bin_index): #x, y에 num을 넣었을 시 
    #exit condition
    if x == -1:
        output.append(sdoku)
        return
    
    #process(filtering)
    #3X3 검증 위함
    if x < 3:
        n = 0
    elif x < 6:
        n = 3
    else:
        n = 6
    
    if y < 3:
        m = 0
    elif y < 6:
        m = 3
    else:
        m = 6      
    
    if num not in sdoku[x]: #가로 체크
        count = 0
        for i in range(9): 
            if sdoku[i][y] == num: #세로체크
                count += 1
        if count == 0:
            count2 = 0
            for k in range(n, n+3): # 3X3 체크
                for l in range(m, m+3):
                    if sdoku[k][l] == num:
                        count2 +=1
            if count2 == 0:
                sdoku[x][y] = num #스도쿠에 수 입력
                            
                #1. 다음 빈칸 찾기
                next_x = bin[bin_index+1][0]
                next_y = bin[bin_index+1][1]
                
                #2. 1~9까지 넣어보기
                for i in range(1, 10):
                    sdoku_f(next_x, next_y, i, bin_index+1)
                     
for i in range(1, 10):
    sdoku_f(bin[0][0], bin[0][1], i, 0)

for i in range(9):
    for j in output[0][i]:
        print(j, end=' ')
    print(" ")

# end_time = time.process_time()
# print(f"time elapsed : {int(round((end_time - start_time) * 1000))}ms")