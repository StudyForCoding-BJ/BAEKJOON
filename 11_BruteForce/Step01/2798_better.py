#BOJ 2798_better
#반복문이 현저하게 적게 돎.
#sort에서 의외로 시간이 오래 걸리지 않는 걸로 보임.

num, target = map(int, input().split())
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)

#Brute Force
res = 0
for i in range(num-2):
    left = i+1
    right = num-1
    while left < right:
        sum = card_list[i] + card_list[left] + card_list[right]
        if target >= sum:
            res = max(res, sum)
            right -= 1
        else:
            left += 1
print(res)