#BOJ 15650 _ lib
#조합(combinations) 사용. O(r(nCr)) => Worst case는 O(n!)에 수렴할 듯
#76ms, 154B

import itertools

end, num = map(int, input().split())
print('\n'.join(list(map(' '.join, itertools.combinations(map(str, list(range(1, end+1))), num)))))