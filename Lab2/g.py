ans = dict()
cnt = 0
n = int(input())
for _ in range(n):
    d, w = input().split()
    if w not in ans.keys():
        ans[w] = 0
    ans[w] += 1
m = int(input())
for _ in range(m):
    h, a, k = input().split()
    if a in ans.keys():
        ans[a] -= int(k)

for v in ans.values():
    if v > 0:
        cnt += v


print(f'Demons left: {cnt}')
