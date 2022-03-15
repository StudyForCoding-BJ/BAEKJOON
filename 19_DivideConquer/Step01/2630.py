#BOJ 2630
import sys

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
blue = 0
white = 0

def check(a:int, ppr: list):
    global blue, white
    
    if a == 1:
        if ppr[0][0] == 0:
            white += 1
        else:
            blue += 1
        return
    
    #check color
    cnt = 0
    for i in range(a):
        cnt += sum(ppr[i])
    if cnt == 0:
        white += 1
    elif cnt == a**2:
        blue += 1
    #keep cut
    else:
        one = []
        two = []
        for j in range(0, a//2):
            one.append(ppr[j][0:a//2])
            two.append(ppr[j][a//2:a])
        check(a//2, one)
        check(a//2, two)
        three = []
        four = []
        for j in range(a//2, a):
            three.append(ppr[j][0:a//2])
            four.append(ppr[j][a//2:a])
        check(a//2, three)
        check(a//2, four)

check(n, paper)
print(white, blue, sep='\n')