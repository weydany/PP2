s = input()
ans = 0
for i in range(len(s)):
    if int(s[i]) == 1:
        ans += 2**(len(s) - i - 1)

print(ans)