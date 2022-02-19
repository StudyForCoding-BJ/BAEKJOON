# 68ms
# 30860KB

import sys
N = int(sys.stdin.readline())

for i in range(N):
    n, m = map(int, sys.stdin.readline().split())
    nu = 1
    de = 1
    # mCn
    for i in range(1, n+1):
        nu *= m - i + 1
        de *= i
    print(nu // de)
