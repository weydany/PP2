import re

s = "decode abbbb"

x = re.search(r'ab*', s)

if x:
    print('ok')
else:
    print('no')