#BOJ 5430
#136ms, print로 쓰면 136ms
import sys
tc = int(input())

def sol(cmd, n, x):
    cmd = cmd.replace("RR", "")
    l = 0
    r = 0
    rev = True
    
    for i in cmd:
        if i == 'R':
            rev = not rev
        else:
            if rev == True:
                l += 1
            else:
                r += 1
    if l+r <= n:
        res = x[l:n-r]
        if rev == True:
            return '['+','.join(res)+']'
        else:
            return '['+','.join(res[::-1])+']'
    else:
        return 'error'

for i in range(tc):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().rstrip()[1:-1].split(',')
    if n == 0: []
    print(sol(cmd, n, x))