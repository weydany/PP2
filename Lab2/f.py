n = int(input())
d = dict()
max = 0
for i in range(n):
    name, money = input().split()
    if name not in d.keys():
        d[name] = 0
    d[name] += int(money)
    if d[name] > max:
        max = d[name]


for k, v in sorted(d.items()):
    if v == max:
        print(f'{k} is lucky!')
    else:
        print(f'{k} has to receive {max - v} tenge')