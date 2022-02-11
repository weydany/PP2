from math import sqrt
px, py = map(int, input().split())
n = int(input())
ans = []
for _ in range(n):
    x, y = map(int, input().split())
    l = sqrt((px - x)**2 + (py - y)**2)
    ans.append([l, x, y])
ans.sort()
for i in ans:
    print(i[1], i[2])