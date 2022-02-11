ans = set()
n = int(input())
for _ in range(n):
    passw = input()
    upper, lower, digit = False, False, False
    for i in passw:
        if i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif i.isdigit():
            digit = True
    
    if upper and lower and digit:
        ans.add(passw)

print(len(ans))
print(*sorted(ans), sep='\n')