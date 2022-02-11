n, f = map(int, input().split())
if n <= 500 and f%2 == 0:
    check = True
    for i in range(2, n):
        if n % i == 0:
            check = False
            break
    
    if check and n >= 2:
        print('Good job!')
    else:
        print('Try next time!')
else:
    print('Try next time!')