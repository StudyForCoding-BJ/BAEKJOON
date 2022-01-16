import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    d = int(sys.stdin.readline().strip())
    data.append(d)

data.sort()

for i in data:
    print(i)

