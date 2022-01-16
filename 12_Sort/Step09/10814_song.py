import sys
N = int(input())

data = []
for i in range(N):
    (age, name) = list(sys.stdin.readline().split())
    data.append((age, name))

data.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(data[i][0], data[i][1])
