from math import prod

base = float(input('Length of base: '))
height = float(input('Height of parallelogram: '))

area = prod([base, height])

print(f'Expected Output: {area}')