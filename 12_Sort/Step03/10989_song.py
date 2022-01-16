import sys

n = int(sys.stdin.readline())

freq = [0] * 10001
for i in range(n):
    freq[int(sys.stdin.readline())] += 1

for j in range(10001):
    if freq[j] != 0:
        for k in range(freq[j]):
            print(j)
