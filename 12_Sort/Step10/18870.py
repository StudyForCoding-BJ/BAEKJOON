#BOJ 18870

size = int(input())
intlist = input().split()
coord = [int(i) for i in intlist]
unique = list(set(coord))
unique.sort()
pair = {}
res = []
for i in range(len(unique)):
    pair[unique[i]] = i
for i in range(size):
    res.append(pair.get(coord[i]))
for i in range(0, size):
    print(res[i], end = ' ')