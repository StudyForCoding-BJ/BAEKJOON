#BOJ 1874
import sys
num = int(input())
st = []
res = []
last = 0

for i in range(num):
    a = int(sys.stdin.readline().strip())
    if len(st) == 0:
        if last < a:
            for j in range(last+1, a+1):
                st.append(j)
                res.append('+')
        else:
            print('NO')
            exit()
    if a == st[-1]:
        st.pop()
        res.append('-')
    else:
        if last < a:
            for j in range(last+1, a+1):
                st.append(j)
                res.append('+')
            st.pop()
            res.append('-')
        else:
            print('NO')
            exit()
    if last < a:
        last = a
print('\n'.join(res))