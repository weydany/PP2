from tabnanny import check


a = list(map(int, input().split()))
for i in range(len(a) - 1):
    if a[i] == 0:
        check = False
        jump = 2
        for j in range(i - 1, -1, -1):
            if a[j] >= jump:
                check = True
                break
            jump += 1
        if not check:
            print(0)
            exit()
print(1)