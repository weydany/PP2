essay = input().split()
ans = set()
for i in essay:
    word = ''
    for char in i:
        if char.isalpha():
            word += char
    ans.add(word)

print(len(ans))
print(*sorted(ans), sep='\n')