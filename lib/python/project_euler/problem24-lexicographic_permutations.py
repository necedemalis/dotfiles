'''Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.'''
from itertools import permutations

perm_list = sorted(list(permutations(['0','1','2','3','4','5','6','7','8','9'],10)))
print(''.join(perm_list[999999]))
