d = dict.fromkeys(['[', ']', '{', '}', '(', ')'], 0)
s = input()
for i in s:
    d[i] += 1

if d['['] == d[']'] and d['{'] == d['}'] and d['('] == d[')']:
    print('Yes')
else:
    print('No')