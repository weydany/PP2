a = list(map(int, input().split()))
for i in range(len(a) - 1):
    if a[i] == 0 and a[i - 1] < 2:
        print(0)
        exit()
print(1)