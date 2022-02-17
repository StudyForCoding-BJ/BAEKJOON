# 72ms
# 30864KB
# 배열 자체에 인출하는데 걸리는 총 시간을 저장

N = int(input())
P = list(map(int, input().split()))

P.sort()

for i in range(1, N):
    P[i] = P[i-1] + P[i]

print(sum(P))