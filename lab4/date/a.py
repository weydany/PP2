from datetime import *

ans = date.today() + timedelta(days=5)
day = ans.strftime('%d')
month = ans.strftime('%m')
year = ans.strftime('%Y')
print(f'{day}.{month}.{year}')