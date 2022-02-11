n = int(input())
books = []
for _ in range(n):
    x = input().split()
    if x == ['2']:
        print(books.pop(0), end=' ')
    else:
        books.append(x[1])