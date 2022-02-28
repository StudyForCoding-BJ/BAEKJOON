#BOJ 1021
from collections import deque
n, m = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque([0 for i in range(n)])

for i in range(m):
    dq[nums[i]-1] = nums[i]

cnt = 0

for i in nums:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)