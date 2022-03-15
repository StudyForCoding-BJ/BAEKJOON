#BOJ 12015
#https://jainn.tistory.com/90
#LIS를 계속 갱신하는 구조. + 기존의 LIS 중 더 작은 숫자가 위치할 수 있는 곳이 있으면 바꿔치기 함 -> 진짜 LIS는 될 수 없는 이유
#진짜 LIS는 아니지만 더 작은 숫자로 바꿔주는 과정 때문에 최종 LIS의 길이는 같을 수 밖에 없음.
#걸어놓은 링크에서 [0, 50, 70, 90]이 [0, 50, 70, 75]로 바뀌었기 때문에 정상적으로 LIS를 추적할 수 있었음
#맨 마지막 요소를 제외하고 안에 있는 것은 어떻게 바뀌든 간에 LIS의 길이 자체에는 영향을 주지 않음.
#그런데 맨 마지막 요소는 계속 낮은 값으로 갱신해줘야 함. 그래야 최대한 긴 부분수열을 가질 수 있음
#이분 탐색이 바로 가지고 있는 LIS에서 지금 넣어줄 요소가 들어갈 위치를 찾는 과정.

n = int(input())
a = list(map(int, input().split()))

memo = [0]

def bin(l: int, r: int, t: int):
    while l<r:
        m = (l+r)//2
        if memo[m] < t:
            l = m+1
        else:
            r = m
    memo[r] = t

for i in a:
    if i > memo[-1]:
        memo.append(i)
    else:
        bin(0, len(memo), i)

print(len(memo)-1)