import sys

N = int(input())

cost = [0] *301
for i in range(1, N+1):
    cost[i] = int(sys.stdin.readline())

result = [0] * 301
result[1] = cost[1]
result[2] = cost[1] + cost[2]
result[3] = max(cost[1] + cost[3], cost[2] + cost[3] )
    
for i in range(4, N+1):
    result[i] = max(cost[i] + cost[i-1] + result[i-3], cost[i] + result[i-2])
        
print(result[N])
