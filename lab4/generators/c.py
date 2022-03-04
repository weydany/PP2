def generator():
    ans = 0
    while True:
        yield ans
        ans += 12

n = int(input())
gen = generator()

while True:
    ans = next(gen)
    if ans > n:
        break
    print(ans)
