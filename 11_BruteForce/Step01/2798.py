#BOJ 2798

num, target = map(int, input().split())
card_list = list(map(int, input().split()))

#Brute Force
start = target
for i in range(num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            res = card_list[i]+card_list[j]+card_list[k]
            if max(target, res) != target:
                continue
            else:
                if min(start, target-res) == start:
                    continue
                else:
                    start = target-res
                    maxSum = res
print(maxSum)