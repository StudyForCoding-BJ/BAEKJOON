#BOJ 2447
#알고리즘 고안 후 출력은 다른 풀이 참조 -> 구현 연습 필요

import sys
sys.setrecursionlimit(10**9)

def draw(a: int):
    if a == 1:
        return "*"
    
    pic = []
    unit = draw(a//3)
    
    for i in unit:
        pic.append(i*3)
    for i in unit:
        pic.append(i + " "*(a//3) + i)
    for i in unit:
        pic.append(i*3)
    
    return pic

#This PART!
print('\n'.join(draw(int(input()))))