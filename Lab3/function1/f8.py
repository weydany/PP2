def spy_game(a: list):
    cnt_zero = 0
    for i in range(len(a)):
        if a[i] == 0:
            cnt_zero += 1
        if a[i] == 7 and cnt_zero >= 2:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))