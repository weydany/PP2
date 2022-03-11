import re

s = 'DecodE'

x = re.search(r'[A-Z]{1}[a-z]+', s)

if x:
    print('ok')
else:
    print('no')