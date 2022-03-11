import re

s = 'aaa_b'

x = re.search(r'[a-z]+_[a-z]+', s)

if x:
    print('ok')
else:
    print('no')