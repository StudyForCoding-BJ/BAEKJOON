#BOJ 1966 _ 3
#76ms
#우선순위 배열 자체를 deque가 아닌 list로 바꿔봄.
#훨씬 적게 걸림
import sys
tc = int(input())
for i in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    idx = list(range(n))
    
    t = idx[m]
    cnt = 0
    
    while True:
        if p[0] == max(p):
            cnt += 1
            if idx[0] == t:
                print(cnt)
                break
            else:
                del p[0]
                del idx[0]
        else:
            p.append(p[0])
            del p[0]
            idx.append(idx[0])
            del idx[0]