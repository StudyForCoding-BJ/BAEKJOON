#124ms
#30864KB

N = int(input())
P = list(map(int, input().split()))

P.sort()
count = 0
for i in range(N):
    temp = 0
    for j in range(i+1):
        temp += P[j]
    count += temp

print(count)