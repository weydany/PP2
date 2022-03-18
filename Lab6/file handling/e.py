with open('test.txt', 'w') as file:
    a = [1, 2, 3, 4]
    for i in a:
        file.write(str(i) + ' ')