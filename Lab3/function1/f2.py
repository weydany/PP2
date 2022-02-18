def convert(f: float):
    return f'{f} Fahrenheit = {(5 / 9) * (f - 32)} Celsius'

f = float(input())
print(convert(f))