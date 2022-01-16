N = int(input())
weight = []
height = []

for i in range(N):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

rank = []
for j in range(N):
    temp = 0
    
    for k in range(N):
        if k == j:
            pass
        elif weight[j] < weight[k] and height[j] < height[k]:
            temp += 1
        else:
            pass
        
    rank.append(temp+1)

for m in range(len(rank)):
    print(rank[m], end=' ')
        
