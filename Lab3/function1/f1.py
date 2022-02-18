def convert(grams: float):
    return f'{grams} grams = {28.3495231 * grams} ounces'

grams = float(input())
print(convert(grams))