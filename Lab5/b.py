import re

s = 'decode abb'

x = re.search(r'ab{2,3}', s)

if x:
    print('ok')
else:
    print('no')