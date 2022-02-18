a = list(map(int, input().split()))
if len(a) == 1:
    n = a[0]
    x = int(input())
else:
    n = a[0]
    x = a[1]
arr = [x + int(i)*2 for i in range(n)]
ans = arr[0]
for i in arr[1:]:
    ans ^= i
print(ans)