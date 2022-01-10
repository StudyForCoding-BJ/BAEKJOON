#BOJ 4153

while True:
    a, b, c  = map(int, input().split())
    size = sorted([a, b, c])
    if a == 0 and b == 0 and c == 0:
        break
    elif size[2]**2 == size[0]**2 + size[1]**2:
        print("right")
    else:
        print("wrong")