#BOJ 17298
#1360ms
import sys
num = int(input())
ori = list(map(int, sys.stdin.readline().split()))
st = [0]
big = [-1]*num
for i in range(1, num):
    while len(st) != 0 and ori[st[-1]] < ori[i]:
        big[st.pop()] = ori[i]
    st.append(i)
print(*big)