#BOJ 1085

def shortcut(x, y, w, h: int):
    if x <= w/2:
        if y <= h/2:
            return min(x,y)
        else:
            return min(x,h-y)
    else:
        if y <= h/2:
            return min(w-x,y)
        else:
            return min(w-x,h-y)
x, y, w, h = map(int,input().split())
print(shortcut(x, y, w, h))