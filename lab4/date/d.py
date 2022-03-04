from datetime import *

date = datetime(2003, 3, 21)
today = datetime.today()

print((today - date).total_seconds())