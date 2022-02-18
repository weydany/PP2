def reverse(s: str):
    ans = s.split()
    return ' '.join(reversed(ans))

s = input()
print(reverse(s))