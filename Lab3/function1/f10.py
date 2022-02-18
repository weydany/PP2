def unique(a: list):
    ans = []
    for i in a:
        if i not in ans:
            ans.append(i)
    return ans

a = list(map(int, input().split()))
print(unique(a))