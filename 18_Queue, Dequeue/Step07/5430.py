#BOJ 5430
#cmd.replace가 여기서 대체 왜 안 되는지 모르겠음
import sys
tc = int(input())

def sol(cmd, n, x):
    cmd.replace("RR", "")
    l = 0
    r = 0
    rev = True
    
    for i in cmd:
        if i == 'R':
            rev = False
        else:
            if rev == True:
                l += 1
            else:
                r += 1
    if l+r <= n:
        res = x[l:n-r]
        if rev == True:
            return '['+','.join(res)+']\n'
        else:
            return '['+','.join(res[::-1])+']\n'
    else:
        return 'error\n'

for i in range(tc):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().rstrip()[1:-1].split(',')
    if n == 0: []
    sys.stdout.write(sol(cmd, n, x))