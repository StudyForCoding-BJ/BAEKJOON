#BOJ 4949
import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == '.':
        exit()
    st = []
    for i in a:
        if i == '[':
            st.append(1)
        elif i == ']':
            if len(st)!= 0 and st[-1] == 1:
                st.pop()
            else:
                st.append(0)
                break
        elif i == '(':
            st.append(2)
        elif i == ')':
            if len(st)!= 0 and st[-1] == 2:
                st.pop()
            else:
                st.append(0)
                break
    if len(st) == 0:
        print('yes')
    else:
        print('no')