import os

if os.path.isdir('C:\\Users\\acer\\OneDrive\\Рабочий стол\\decode'):
    print('Exists')
    for dirpath, dirnames, filenames in os.walk('C:\\Users\\acer\\OneDrive\\Рабочий стол\\decode'):
        for dirname in dirnames:
            print('Каталог: ', os.path.join(dirpath, dirname))
else:
    print('Not exists')