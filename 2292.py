#BOJ 2292

def depth(a: int):
    start = 1
    for i in range (1, 18258):  #Equation
        #print(i)
        start += i*6
        #print(start)
        if a <= start:
            if a == 1:
                return 1
            else:
                return i+1  # +1 for Depth No 1 room

end = int(input())
print(depth(end))