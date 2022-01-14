#BOJ 2869

up, down, tree = map(int, input().split())
if (tree-up)%(up-down) == 0:
    print(((tree-up)//(up-down))+1)
else:
    print(((tree-up)//(up-down))+2)