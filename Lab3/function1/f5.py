def print_perm(s: str):
    from itertools import permutations
    for i in list(permutations(s)):
        print(*i, sep='')

s = input()
print_perm(s)
