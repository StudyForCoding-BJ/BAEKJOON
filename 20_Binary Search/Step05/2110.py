#BOJ 2110
#다른 풀이 참조
#말 그대로 가장 인접한 거리를 이분탐색. 그래서 x[i] - prev >= m이 조건.
#이전의 집과 다음에 공유기를 둘 집 사이의 거리가 최소한 m 이상이어야 한다는 뜻
#그런 식으로 for loop를 돌려서 공유기를 한 대씩 설치(cnt+=1) 다 설치했으면 m값끼리 비교
#l, r, m은 집 좌표랑 관련된 게 아니라 인접한 거리의 후보일 뿐
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = list(int(input()) for i in range(n))
x.sort()
res = 0

def bin(l: int, r: int):
    global res
    while l <= r:
        m = (l+r)//2
        cnt = 1
        prev = x[0]
        for i in range(1, n):
            if x[i] - prev >= m:
                cnt += 1
                prev = x[i]
        
        if cnt >= c:
            res = max(res, m)
            l = m+1
        
        else:
            r = m-1
bin(1, x[-1]-x[0])
print(res)