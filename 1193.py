#BOJ 1193

def fraction(a: int):
    start = 0
    for depth in range (1, 44721):
        start += depth
        if a <= start:
            gap = start - a
            if depth%2 == 0:
                print(depth)
                return (str(depth-gap)+"/"+str(1+gap))
            else:
                return (str(1+gap)+"/"+str(depth-gap))

print (fraction(int(input())))