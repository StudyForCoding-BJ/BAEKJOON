#BOJ 17298 _ 2
#1536ms
import sys
num = int(input())
ori = list(map(int, sys.stdin.readline().split()))
st = []
big = [-1]*num
for i in range(num):
    while len(st) != 0 and st[-1][1] < ori[i]:
        big[st.pop()[0]] = ori[i]
    st.append((i, ori[i]))
print(*big)