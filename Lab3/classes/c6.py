def filter(a: list):
    ans = []
    check = lambda x: x >= 2
    div = lambda x, y: x % y == 0
    for elm in a:
        cnt = 0
        for i in range(2, elm):
            if div(elm, i):
                cnt += 1

        if check(elm) and cnt == 0:
            ans.append(elm)
    
    return(ans)

print(filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))