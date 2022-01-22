#BOJ 15649 _ lib
#순열(permutation) -> 시간 복잡도: O(n!) 그래서 표본 크기가 커지면 적합하지는 않을 것으로 보임.
#80ms, 154B

import itertools

end, num = map(int, input().split())
print('\n'.join(list(map(' '.join, itertools.permutations(map(str, list(range(1, end+1))), num)))))