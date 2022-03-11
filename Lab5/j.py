import re

s = 'ThisIsACamelCase'
s = re.sub(r'(?<!^)(?=[A-Z])', '_', s)
s = s.lower()
print(s)