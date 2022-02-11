s = list(map(str, input()))
i = 0
while i < len(s):
    if i + 1 < len(s) and ((s[i] == '[' and s[i + 1] == ']') or (s[i] == '{' and s[i + 1] == '}') or (s[i] == '(' and s[i + 1] == ')')):
        s.pop(i)
        s.pop(i)
        i -= 1
    i += 1

if len(s) == 0:
    print('Yes')
else:
    print('No')