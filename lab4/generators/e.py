def generator(n: int):
    ans = n
    while n >= 0:
        yield ans
        ans -= 1

n = int(input())
gen = generator(n)
while True:
    ans = next(gen)
    print(ans)
    if ans == 0:
        break
