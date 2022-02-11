n = int(input())
for i in range(1, n + 1):
    if n % 2 == 1:
        print('.'*(n - i), end='')
        print('#'*i)
    else:
        print('#'*i, end='')
        print('.'*(n - i))