#BOJ 9012
import sys
num = int(input())

for i in range(num):
    string = sys.stdin.readline().strip()
    st = []
    for i in string:
        if i == '(':
            st.append(1)
        else:
            if len(st) != 0 and st[0]!=0:
                st.pop()
            else:
                st.append(0)
    if len(st) == 0:
        print("YES")
    else:
        print("NO")