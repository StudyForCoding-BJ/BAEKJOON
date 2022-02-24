#BOJ 13305
import sys

city = int(input())
d = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

init = 0
minimum = 1000000001
for i in range(0, city-1):
    minimum = min(minimum, cost[i])
    init += minimum * d[i]
print(init)