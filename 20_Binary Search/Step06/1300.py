#BOJ 1300
#앞 숫자가 특정 개수가 있는 지점을 찾는 이분탐색.
#이분탐색은 보통의 탐색 시간을 줄이기 위한 건데 일반적인 for문으로 탐색했다면
#배열 A를 다 돌아서 O(N^2)의 시간이 걸렸을 것
#getIdx를 가지고 배열 A를 돈다면 사실상 O(N^3)이고 만약 일반적인 탐색을 썼다면 getIdx를 돌리기보다는
#배열 A를 다 돌면서 리스트에 저장하고 sort하는 방법을 썼을것임(그게 더 효율적이니까)
#그래도 여전히 O(N^2)을 벗어날 수는 없고
#이 알고리즘은 O(NlogN). 이분탐색이 O(logN), getIdx가 O(N)

n = int(input())
k = int(input())

def bin(l: int, r: int, t: int):
    res = 0
    while l <= r:
        m = (l+r)//2
        if getIdx(m) >= t:
            res = m
            r = m-1
        else:
            l = m+1
    return res
        
def getIdx(a: int):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(a//i, n)
    return cnt

print(bin(1, k, k))