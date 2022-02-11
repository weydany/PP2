n = int(input())
z = input()
if z == 'b':
    print(n * 1024)
else:
    c = int(input())
    ans = n / 1024
    print(f'{ans:.{c}f}')