s = input()
char = input()
ans = []
for i in range(len(s)):
    if s[i] == char:
        ans.append(i)

if len(ans) == 1:
    print(ans[0])
else:
    print(ans[0], ans[-1])