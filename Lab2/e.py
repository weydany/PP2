n, x = map(int, input().split())
arr = [x + int(i)*2 for i in range(n)]
ans = arr[0]
for i in arr[1:]:
    ans ^= i
print(ans)