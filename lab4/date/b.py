from datetime import *

yesterday = date.today() - timedelta(days=1)
today = date.today()
tomorrow = date.today() + timedelta(days=1)

print('Yesterday:', yesterday)
print('Today:', today)
print('Tomorrow:', tomorrow)