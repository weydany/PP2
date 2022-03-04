from re import A


def generator(a: int, b: int):
    ans = a
    while ans <= b:
        yield ans
        ans += 1

a, b = map(int, input().split())
gen = generator(a, b)

for _ in range(b - a + 1):
    print(next(gen))