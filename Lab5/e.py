import re

s = 'a#b'

x = re.search(r'a.b$', s)

if x:
    print('ok')
else:
    print('no')