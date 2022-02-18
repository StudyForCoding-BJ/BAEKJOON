#BOJ 15652 _ lib
#72ms, 196B. 메모리 동일

from itertools import combinations_with_replacement

end, num = map(int, input().split())
print('\n'.join(list(map(' '.join, combinations_with_replacement(map(str, list(range(1, end+1))), num)))))