# 72ms
# 30864KB

import sys
n, m = map(int, sys.stdin.readline().split())

def cnt(n, k):
    cnt = 0
    while n > 0:
        n = n // k
        cnt += n
        
    return cnt

cnt_2 = cnt(n, 2) - cnt(m, 2) - cnt(n-m, 2)
cnt_5 = cnt(n, 5) - cnt(m, 5) - cnt(n-m, 5)

print(min(cnt_2, cnt_5))  

# 팩토리얼 0의 개수 세는 알고리즘 참고: https://lucian-blog.tistory.com/84?category=1034989