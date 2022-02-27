import sys

# 코드 리뷰
table_len, target_len = map(int, sys.stdin.readline().split())
queue = [i + 1 for i in range(table_len)]

result = 0
for find in list(map(int, sys.stdin.readline().split())):
    idx = queue.index(find)
    # 길이만큼 회전시키면 된다.
    result += min(len(queue[idx:]), len(queue[:idx]))
    # 합치는 순서는 상관이 없다. 앞으로 붙이나, 뒤로 붙이나 똑같음
    queue = queue[idx + 1:] + queue[:idx]

print(result)