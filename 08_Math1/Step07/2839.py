#BOJ 2839

def sack(n: int):
    pair = []
    for a in range ((n//3)+1):
        if (n - 3*a) % 5 == 0:
            b = (n - 3*a) // 5
            pair.append(a+b)
        else:
            continue
    if len(pair) == 0:
        pair.append(-1)
    return pair
print(min(sack(int(input()))))