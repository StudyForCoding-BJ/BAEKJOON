#3260ms
#153692KB

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
            bin.append((i, j))

output = []   

def checkRow(x, num):
    for i in range(9):
        if sdoku[x][i] == num:
            return False
    return True

def checkCol(y, num):
    for i in range(9):
        if sdoku[i][y] == num:
            return False
    return True

def check33(x, y, num):
    #3X3 검증 위함
    n = x // 3 * 3
    m = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sdoku[n+i][m+j] == num:
                return False
    return True
    
def sdoku_f(bin_index):
    #1. exit condition
    if bin_index == len(bin):
        for i in range(9):
            print(*sdoku[i])
        exit(0) #return으로 하면 모든 경우의 수 출력함
    
    #2. process(filtering)
    for num in range(1, 10):
        x = bin[bin_index][0]
        y = bin[bin_index][1]
        
        if checkRow(x, num) and checkCol(y, num) and check33(x, y, num):
                sdoku[x][y] = num #스도쿠에 수 입력
                #3. recursion
                sdoku_f(bin_index+1)
                sdoku[x][y] = 0 # 못들어가면 스도쿠 초기화
                    
sdoku_f(0)

'''
#1. exit condition 에서 
for i in range(9):
    print(*sdoku[i])
로 sdoku를 바로 출력하면 정상적으로 풀이된 sdoku식을 출력함

반면 #1. exit condition 에서 
output.append(sdoku)으로 output배열에 sdoku객체를 넣고 함수실행이 끝난 뒤 
output을 출력하면 0으로 초기화된 원본 스도쿠판을 출력함

이는 output.append(sdoku)할때 해당 배열 값을 저장하는게 아니라 sdoku객체를 저장하기 때문에
함수 밖에서 output을 출력하면
마지막 함수 실행이 끝날 때 sdoku[x][y] = 0 문으로 초기화 된 sdoku값이 출력되는 것. 

'''