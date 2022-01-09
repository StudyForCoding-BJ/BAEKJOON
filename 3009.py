#BOJ 3009

x = [] * 3
y = [] * 3
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
print (sum(list(set(x)))*2-sum(x), sum(list(set(y)))*2-sum(y))