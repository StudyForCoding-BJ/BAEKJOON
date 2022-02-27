#BOJ 11399

num = int(input())
time = list(map(int, input().split()))
time.sort()
res = 0
for i in range(num):
    res += time[i]*(num-i)
print(res)