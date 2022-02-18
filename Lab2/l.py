s = input()
a = [s[0]]
for i in s[1:]:
    if i == ')' and a[len(a) - 1] == '(':
        a.pop(len(a) - 1)
    elif i == '}' and a[len(a) - 1] == '{':
        a.pop(len(a) - 1)
    elif i == ']' and a[len(a) - 1] == '[':
        a.pop(len(a) - 1)
    else:
        a.append(i)

if len(a) == 0:
    print('Yes')
else:
    print('No')