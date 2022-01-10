#BOJ 9020

def era(start, end: int):
    era = [1]*(end+1)
    era[1] = 0

    for i in range(2, int(end**0.5)+1):
        if era[i] == 1:
            for j in range(i*2, end+1, i):
                era[j] = 0

    primelist = []
    for i in range(start, end+1):
        if era[i] == 1:
            primelist.append(i)
    return primelist

for i in range(int(input())):
    even = int(input())
    total = era(2, even)
    for j in range(int(even/2), 1, -1):
        if j in total:
            if even-j in total:
                print (j, even-j)
                break

"""
에라토스테네스의 체 시간복잡도: O(NloglogN)
O(NloglogN)은 O(1)에 가까울정도로 단순

범위 제한이 있을 경우엔 범위에 맞게 리스트를 먼저 구한 뒤에 처리하는게 빠름

참고: https://continuous-development.tistory.com/204
"""
            
