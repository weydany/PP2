ans = []
while True:
    date = input().split()
    if date == ['0']:
        break
    ans.append([date[2], date[1], date[0]])
for i in sorted(ans):
    print(*reversed(i))