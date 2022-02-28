#BOJ 17298 _ 3
#1512ms
import sys
num = int(input())
ori = list(map(int, sys.stdin.readline().split()))
st = []
big = [-1]*num
for i in range(num):
    while len(st) != 0 and st[-1][0] < ori[i]:
        big[st.pop()[1]] = ori[i]
    st.append((ori[i], i))
print(*big)