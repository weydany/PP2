ans = []
while True:
    n = int(input())
    if n == 0:
        break
    ans.append(n)
i = 0
while i <= len(ans) - i - 1:
    if i == len(ans) - i - 1:
        print(ans[i])
        break
    else:
        print(ans[i] + ans[len(ans) - i - 1], end=' ')
    i += 1