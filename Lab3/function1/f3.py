def rabbits_and_chickens(heads: int, legs: int):
    for i in range(1, heads + 1):
        if i * 2 + (heads - i) * 4 == legs:
            return f'{i} rabbits\n{heads - i} chickens'

heads, legs = map(int, input().split())
print(rabbits_and_chickens(heads, legs))
