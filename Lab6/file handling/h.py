import os

if os.path.isfile('output.txt'):
    os.remove('output.txt')
    print('file deleted')
else:
    print('file not exist')