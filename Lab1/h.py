s = input()
n = int(input())
ans = []
for i in range(len(s)):
    if int(s[i]) == n:
        ans.append(i)

if len(ans) == 1:
    print(ans[0])
else:
    print(ans[0], ans[-1])