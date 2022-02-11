n = int(input())
a = list(map(int, input().split()))
max = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] * a[j] > max:
            max = a[i] * a[j]

print(max)