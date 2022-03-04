from math import prod

height = float(input('Height: '))
first = float(input('Base, first value: '))
second = float(input('Base, second value: '))

area = prod([first + second, height]) / 2

print(f'Expected Output: {area}')