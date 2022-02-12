#96ms

from itertools import permutations
N, M = map(int, input().split())
arr = list(range(1, N+1))

'''
list(itertools.permutations(['1', '2', '3'], 2)) 
-> [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
'''
result = list(map(' '.join,  permutations(map(str, arr), M)))

for i in range(len(result)) :
    print(result[i])