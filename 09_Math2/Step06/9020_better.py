#BOJ 9020

def era(start, end: int):
    era = [1]*(end+1)
    era[1] = 0

    for i in range(2, int(end**0.5)+1):
        if era[i] == 1:
            for j in range(i*2, end+1, i):
                era[j] = 0

    return era

for i in range(int(input())):
    even = int(input())
    total = era(1, even)
    a = even//2
    b = a
    for j in range(even):
        if total[a]==1 and total[b] == 1:
            print(a,b)
            break
        a -= 1
        b += 1

"""
에라토스테네스의 체 시간복잡도: O(NloglogN)
O(NloglogN)은 O(1)에 가까울정도로 단순
범위 제한이 있을 경우엔 위의 풀이처럼 범위에 맞게 리스트를 먼저 구한 뒤에 처리하는게 빠름
참고: https://continuous-development.tistory.com/204
"""
          
